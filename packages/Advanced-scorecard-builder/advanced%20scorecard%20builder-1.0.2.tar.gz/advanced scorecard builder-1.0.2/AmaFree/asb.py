#!/usr/bin/env python3
# -*-coding: utf-8 -*-
"""
AMA Institute
Advanced Scorecard Builder
Free 1.0.2 Version
Authors: Sebastian Zajac <s.zajac@amainstitute.pl>
"""
# =============================================================================
# Libraries
# =============================================================================
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import roc_auc_score as auc
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn import tree
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LogisticRegressionCV
from regressors import stats
# =============================================================================
# Constants Errors
# =============================================================================
ERR_ABT                     = 'Your ABT is not a Pandas DataFrame.\n \
(REMEMBER about na_values in Your read method)'
ERR_TARGET_NAME             = "There is not a target name in DataFrame"
ERR_TARGET_INT              = "Your target column is not int or you have NaN values. \n \
Please use: df = df.dropna(subset=[target_name]) \n \
df[target_name] = df[target_name].astype(np.int64)"
ERR_TARGET_NUMBER           = "You should have just two elements (0 and 1) in target column"
RM_ONE_VALUE                = 'one value in column'
ERR_SCORECARD               = "generate scorecard by fit() method"
BINS_ERR                    = 'Number of bins must be greater then 1'
PRESELECTION_ERR            = 'NO FEATURES AFTER PRESELECTION'
SELECTION_ERR               = 'NO FEATURES AFTER SELECTION'
ERR_GINI_MODEL              = "You don't have model yet"
ERR_TEST_SIZE               = "Test size should be between 0-1"
# =============================================================================
# selection parameters
# =============================================================================
NUM_OF_FEATURES             = 8    # how many features you get from selection method
SELECT_METHOD               = LogisticRegression()  # model for features selection
TEST_SIZE                   = 0.3  # size of test sample, train = 1-TEST_SIZE
RANDOM_STATE                = 1234 # Random seed
N_BINS                      = 4    # max number of categories
MIN_WEIGHT_FRACTION_LEAF    = 0.05 # min percent freq in each category 
MIN_GINI                    = 0.05 # min gini value for preselection
DELTA_GINI                  = 0.2  # max AR Diff value
# =============================================================================
# ASB free ver 1.0.1
# =============================================================================


class AdvancedScorecardBuilder(object):
    """ Advanced ScoreCard Builder Free Version
    Parameters
    ----------
    df: DataFrame, abt dataset. With one target column

    target_name: string, target column name   
        
    dates: string or list, optional (default=None)
     A date type columns list

    Return
    ------
    data: Pandas DataFrame, shape=[n_sample,n_features]  
          data without target
    target_name: string, target column name
    target: 1d NumPy array
       
    _removed_features: dict with removed features from data - one value 
    
    if dates is not None
    _date_names: str, list of date column names
    _date_columns: Numpy array with date type column

    
    Examples
    --------

    >>> import pandas as pd
    >>> from AmaFree import AdvancedScorecardBuilder as asb
    >>> from sklearn import datasets
    >>> X,y = datasets.make_classification(n_samples=10**4, n_features=15, random_state=123)
    >>> names = []
    >>> for el in range(15):
    >>>     names.append("zm"+str(el+1))
    >>> df = pd.DataFrame(X, columns=names)
    >>> df['target'] = y
    >>> foo = asb(df,'target')
    >>> foo.fit()
    >>> foo.get_scorecard()

    Default parameters for fit() method
    -----------------------------------

    test size = 0.3 , train size = 0.7
    Maximal number of bins = 4
    Weight Fraction of category = 0.05 (5%) of all data
    Number of features for model  = 8 
    minimal accepted gini = 0.05 (5%) for one feature
    maximal accepted delta gini = 0.2 
    
    After fit() method You have
    ----------------------------
    train_ - training set with target
    test_  - test set with target
    labels_ - dict with all bin labels
    stats_  - statistics for all features (train)
    stats_test_ - 
    preselected_features
    _rejected_low_gini
    _rejected_AR_gini
    selected_features
    model_info_
    self._scorecard_
    """

    def __init__(self, df, target_name, dates=None):
        """init method
        load abt data as DataFrame and choose column name for target.
        All columns with date put as list in dates parameter.
        """
        # check is df a dataFrame   
        if not isinstance(df, (pd.DataFrame)):
            raise Exception(ERR_ABT)
        self.DESCR = self.__doc__    
        # check if target is ok    
        if self.__check_target(df, target_name):
            self.target_name = target_name # string
            self.target = df[target_name].values # Numpy array
        # remove one unique value columns
        self._removed_features = {}
        self._log = ''
        df = df.drop(self.__get_one_value_features(df), axis = 1)
        # date type data
        if dates:
            self._date_names = dates
            self._date_columns = pd.to_datetime(df[dates], format = '%Y%m')
            df = df.drop(dates, axis=1)
        # categorical features for analysis
        obj_df = df.select_dtypes(include = ['object']).copy()
        c_list = list(obj_df)
        if len(c_list) > 0:
            self._category_df = {}
            for feature in c_list:
                le = LabelEncoder()
                try:
                    le.fit(df[feature])
                    self._category_df[feature] = le
                # code for future categorical data analysis    
                except:
                    raise Exception("Your categorical data have NaN") 
        # remove target from data    
        self.__data_ = df # data with target column
        self.data = df.drop(self.target_name, axis = 1)
        # features without target, dates and one value columns
        self.feature_names = list(self.data)

    def __check_target(self, df, target):
        ''' init HELPER method
        target checker: verify if target name is in df,
        verify if target column is int, 
        verify if there are two unique values in column,
        and if this two values are 1 and 0.
        '''
        if target not in list(df):  # verify target name in df
            raise Exception(ERR_TARGET_NAME)
        if not df[target].dtype in ['int64', 'int32']:  # verify if target column is int
            raise Exception(ERR_TARGET_INT)
        if not len(df[target].unique()) == 2:  # and is there 2 unique values in column
            raise Exception(ERR_TARGET_NUMBER)
        # if this two values are 1 and 0
        if not any(df[target] == 0) & any(df[target] == 1):
            raise Exception(ERR_TARGET_NUMBER)
        return True

    def __get_one_value_features(self, df):
        ''' init  HELPER method
        Take list with bad (one value) features
        '''
        rm_list = []
        for feature in list(df):
            if not len(df[feature].unique()) > 1:
                print('feature {} removed - one value in column'.format(feature))
                self._log += 'feature '+str(feature)+ ' removed - one value in column \n'
                rm_list.append(feature)
                self._removed_features[feature] = RM_ONE_VALUE
        return rm_list
    
    def __str__(self):
        ''' Just for FUN '''
        return '<AMA Institute | Free ASB>'

    def fit(self,
            test_size=TEST_SIZE,
            min_freq_of_category=MIN_WEIGHT_FRACTION_LEAF,
            n_category=N_BINS,
            min_gini= MIN_GINI,
            delta_gini=DELTA_GINI,
            n_features=NUM_OF_FEATURES):
        """ Made score card and model for data

        Parameters
        ----------
        test_size:  float, optional (default=0.3)
            Should be between 0.0 and 1.0 represent the proportion
            of the dataset to include in the test split.

        min_freq_of_category: float, optional (default = 0.05)
            percent of data in each category. 

        n_category: int, maximum of category number in binning.

        min_gini:   float, (default = 0.05) gini minimum value for preselection.

        delta_gini: float, (default = 0.2) AR value for camparision train and test statistics.
        
        n_features: int, maximum number of selected features

        Return
        ------
        self.train_ - training set with target
        self.test_  - test set with target
        self.labels_ - dict with all bin labels
        self.stats_  - 
        self.stats_test_
        self.preselected_features
        self._rejected_low_gini
        self._rejected_AR_gini
        self.selected_features
        self.model_info_
        self._scorecard_            
        """
        # 1. NaN < 0.05 remove
        self._log += 'NaN analysis \n'
        if self.__data_.isnull().any().any():
            self.__data_ = self.__remove_empty_nan(self.__data_, min_freq_nan=min_freq_of_category)
        # 2. split data
        self._log += 'Spliting data \n'
        self.train_, self.test_ = self.__split_frame(test_size=test_size)       
        
        # 3. binning features
        self._log += 'binning features\n'
        trainBin_, testBin_, self.labels_ = self.__sup_bin_features(self.train_, self.test_, self.feature_names, n_category) 
        self._log += 'NaN analysis'
        self.trainBin_, self.testBin_ = self.__fillnan(trainBin_,testBin_,min_freq_nan=min_freq_of_category)
       
        # stats
        self._log += 'Get features stats for training set\n'
        self.stats_ = self.__stats(self.trainBin_,list(self.trainBin_))
        self._log += 'Get features stats for test set\n'
        self.stats_test_ = self.__stats(self.testBin_,list(self.testBin_))
        
        # 4 preselekcja 
        self._log += 'Preselection\n'
        self.preselected_features, self._rejected_low_gini, self._rejected_AR_gini= self.__preselection(list(self.trainBin_),min_gini,delta_gini)
        self._log += 'low gini: '+" ".join(str(x) for x in self._rejected_low_gini)+'\n'
        self._log += 'Delta AR gini: '+" ".join(str(x) for x in self._rejected_AR_gini)+'\n'
        if not len(self.preselected_features):
            self._log += PRESELECTION_ERR
            raise Exception(PRESELECTION_ERR)
         
        trainLogit = self.__logit_value(self.trainBin_[self.preselected_features],self.stats_)
        testLogit = self.__logit_value(self.testBin_[self.preselected_features],self.stats_test_)
        
        # 5 selected features from logit train data
        self.selected_features = self.__selection(trainLogit, n=n_features)  # list
        if not len(self.selected_features):
            self._log += SELECTION_ERR
            raise Exception(SELECTION_ERR)
        self.leader, self.model_info_ = self.__get_model_info(
            trainLogit[self.selected_features], self.train_[self.target_name],testLogit[self.selected_features],self.test_[self.target_name])
        self._scorecard_ = pd.DataFrame.from_dict(self.__scorecard_dict(
            self.selected_features, self.stats_, self.model_info_['coef'], self.model_info_['intercept']))
        
    def __split_frame(self, test_size):
        """Sampling data by random method
        We use sklearn train_test_split method

        Parameters
        ----------
        test_size: float, optional (default=0.3)
            Should be between 0.0 and 1.0 represent the proportion
            of the dataset to include in the test split.

        Return
        ----------
        train_:   DataFrame, shape = [n_samples, (1-test_size)*n_features with target]
        test_:    DataFrame, shape = [n_samples, test_size*n_features with target]

        """
        if test_size <=0 and test_size >=1:
            raise Exception(ERR_TEST_SIZE)
        tr, te = train_test_split(self.__data_, random_state = RANDOM_STATE, test_size=test_size)
        return tr.reset_index(drop=True), te.reset_index(drop=True)

    def __remove_empty_nan(self,df,min_freq_nan):
        df_new = df.copy()
        nAll = df_new.shape[0]
        for feature in list(df_new):
            if df_new[feature].isnull().any():
                nNan = df_new[feature].isnull().sum()
                if nNan/nAll < min_freq_nan:
                    print("You have less then {} empty values in {}. I change them by mean value".format(min_freq_nan,feature))
                    self._log += 'You have less then '+ str(min_freq_nan)+ ' empty values in '+feature+'. I change them by mean value\n'
                    df_new[feature] = df_new[feature].fillna(df_new[feature].mean())
                else:
                    self._log += 'in {} you have more then {} NaNs \n'.format(feature,min_freq_nan)    
        return df_new
    
    def __is_numeric(self, df, name):
        """helper method 
        verify is type of column is int or float
        Parameters
        ----------
        df: DataFrame
        name: string, column name to check
        Return
        ------
        True if column is float or int
        or False if not
        """
        if df[name].dtype in ['int64', 'int32']:
            return True
        if df[name].dtype in ['float64', 'float32']:
            return True
        return False
    
    def __binn_continous_feature(self,df,feature,max_leaf_nodes,
                                min_weight_fraction_leaf=MIN_WEIGHT_FRACTION_LEAF,
                                random_state=RANDOM_STATE):
        """supervised binning of continue feature by tree 

        Parameters
        ----------
        df:                         DataFrame, 
        feature:                    string, analysing feature name
        max_leaf_nodes:             parameter of tree
        min_weight_fraction_leaf:   parameter of tree
        random_state:               parameter of tree

        Return
        ------
        labs: dict, description
        """ 
        # new DataFrame with result
        df_cat = pd.DataFrame()  
        # cut all data to two col DataFrame
        df_two_col = df[[self.target_name, feature]].copy()
        # drop nan values (because tree)
        df_two_col = df_two_col.dropna(axis=0).reset_index(drop=True)
        # binns list with [min,max]
        bins = [-np.inf, np.inf]
        # get Tree classifier - check if we need another parameters !!
        clf = tree.DecisionTreeClassifier(
            max_leaf_nodes=max_leaf_nodes,
            min_weight_fraction_leaf=min_weight_fraction_leaf,
            random_state=random_state) 
        # fit tree
        clf.fit(df_two_col[feature].values.reshape(-1, 1), df_two_col[self.target_name])
        # get tresholds and remove empty
        thresh = [round(s, 3) for s in clf.tree_.threshold if s != -2]  
        # add tresholds to binns
        bins = bins + thresh  
        
        return sorted(bins)

    @staticmethod
    def __cut_bin(data,bins):
        """helper method """
        return pd.cut(data,bins=bins, labels=False, retbins=True, include_lowest=True)

    def __sup_bin_features(self, df,testdf,features,n_bins):
        """binn method
        binning of numerical variables by tree algorithm

        Parameters
        ----------
        df: train DataFrame with data for binning
        testdf: test DataFrame with data for binning
        features: features list
        n_bins: binns number

        Return
        ------
        Binned train set, test set and labels of bins
        """
        df_c = pd.DataFrame() # category frame with labels int
        df_test = pd.DataFrame() # df after bin before checking
        # remove_list = []
        labs = {} # binns lists
        df_copy = df.copy() # copy of data
        df_test_copy = testdf.copy() # copy test data
        # run loop for every feature in data - all should be numeric
        for feature in features:
            # check is type is numeric
            if self.__is_numeric(df_copy, feature):
                labs[feature] = self.__binn_continous_feature(df_copy, feature,n_bins)
                if len(labs[feature])>2:
                # cuts with int labels
                    df_c[feature], _ = self.__cut_bin(df_copy[feature],labs[feature])
                    df_test[feature], _ = self.__cut_bin(df_test_copy[feature],labs[feature])
                elif len(df_copy[feature].unique())==2:
                    df_c[feature] = df_copy[feature]
                    df_test[feature] = df_test_copy[feature]
                else:
                    print('I removed {} - no binns'.format(feature))
                    self._log +=  'I removed '+ str(feature)+' - no binns \n'
                    self._removed_features[feature] = 'no binns'    
            else: # if is category type data or something else
                df_c[feature] = df_copy[feature]
                df_test[feature] = df_test_copy[feature]
                # raise Exception('You still have non numerical data')
        # remember add target to the train and test data
        df_c[self.target_name] = df[self.target_name]
        df_test[self.target_name] = testdf[self.target_name]      
        return df_c, df_test, labs

    def __fillnan(self,df, df_2,min_freq_nan):
        ''' change all nan as last numerical category
        '''
        if not (df.isnull().any().any() and df_2.isnull().any().any()):
            return df, df_2
                
        for feature in df.columns[df.isnull().any()].tolist():
            self._log += 'change NaN values for binned feature '+str(feature) +'\n'
            if df[feature].isnull().sum()/df[feature].shape[0] > min_freq_nan:
                self._log += 'more then '+str(min_freq_nan)+' NaN goes to the NEW category \n'
                df[feature]=df[feature].fillna(df[feature].max()+1)
                df_2[feature]=df_2[feature].fillna(df_2[feature].max()+1)
            else:
                self._log += 'less then '+str(min_freq_nan)+' NaN goes to the FIRST category \n'
                df[feature]=df[feature].fillna(0)
                df_2[feature]=df_2[feature].fillna(0)
        for feature in df_2.columns[df_2.isnull().any()].tolist():
            self._log += 'change NaN values for binned feature '+str(feature) +'\n'
            if df_2[feature].isnull().sum()/df_2[feature].shape[0] > min_freq_nan:
                self._log += 'more then '+str(min_freq_nan)+' NaN goes to the NEW category \n'
                df[feature]=df[feature].fillna(df[feature].max()+1)
                df_2[feature]=df_2[feature].fillna(df_2[feature].max()+1)
            else:
                self._log += 'less then '+str(min_freq_nan)+' NaN goes to the FIRST category \n'
                df[feature]=df[feature].fillna(0)
                df_2[feature]=df_2[feature].fillna(0)            
        return df, df_2    
    
    def __dictStats(self,df,feature):
        ''' Generate dict with target values for feature
        '''
        slownik = {} 
        elements = list(df[feature].unique())
        for el in elements:
                slownik[el] = dict(df[df[feature] == el][self.target_name].value_counts())
                if 0 not in slownik[el]:
                    slownik[el][0] = 0.00000000000000000001
                if 1 not in slownik[el]:
                    slownik[el][1] = 0.00000000000000000001
        return slownik
       
    def __df_stat(self,fd,td,feature):
        ''' Generate DataFrame for feature stats
        '''
        result = pd.DataFrame.from_dict(fd, orient='index')
        #population
        pop_all = result[0]+result[1]
        result['Population'] = pop_all
        result['Percent of population [%]'] = round((pop_all)/ td['length'] , 3)*100
        result['Good rate [%]'] = round(result[0] / pop_all,3)*100
        result['Bad rate [%]'] = round(result[1] / pop_all,3)*100
        p_goods_to_all_goods = result[0] / td[0]
        p_bads_to_all_bads = result[1]/td[1]
        result['Percent of goods [%]'] = round(p_goods_to_all_goods,3)*100
        result['Percent of bad [%]'] = round(p_bads_to_all_bads,3)*100
        result['var'] = feature
        result['logit'] = np.log(result[1] / result[0])
        result['WoE'] = np.log((p_goods_to_all_goods)/(p_bads_to_all_bads))
        result['IV'] =((p_goods_to_all_goods)-(p_bads_to_all_bads))*result['WoE']
        if hasattr(self, '_category_df'):
            if feature in self._category_df:
                result['label'] = str(feature)+' = '+result.index
            else:
                result['label'] = self.__category_names(result,self.labels_[feature],feature)    
        else:    
            result['label'] = self.__category_names(result,self.labels_[feature],feature)
        result = result.rename(columns = { 1:'n_bad', 0:'n_good'})

        result['bin_label'] = result.index
        return result
    
    def __category_names(self, df, bins, name):
        '''helper method for getting bins labels as a string'''
        result = []
        string = ""
        if len(df)==2 and len(bins)==2:
            return [str(name)+"=0",str(name)+"=1"]
        if len(df)==2 and len(bins)==3 and bins[1]==0.5:
            return [str(name)+"=0",str(name)+"=1"]

        if not len(df) == len(bins):
            string = "(not missing) and "
      
        for ix, el in enumerate(bins):
            if ix == 0:
                continue
            if ix == 1:
                string += str(name) + ' <= ' + str(el)
                result.append(string)
                string = str(el) + ' < ' + str(name)
            if ix < len(bins)-1 and ix > 1:
                string += ' <= ' + str(el)
                result.append(string)
                string = str(el) + ' < ' + str(name)
            if ix == len(bins)-1:
                result.append(str(bins[ix-1]) + ' < ' + str(name))

        if len(df) == len(bins):
            result.append('missing')       
        return result

    def __stats(self,df,features):
        '''Generate stats for all features
        '''
        statsDict = {}
        logit_dict = {}
        if self.target_name in features:
            features.remove(self.target_name)  
        target_dict = df[self.target_name].value_counts()
        if 1 not in target_dict.keys():
            target_dict[1] = 0.00000000000000000001
        if 0 not in target_dict.keys():
            target_dict[0] = 0.00000000000000000001
        target_dict['length'] = df.shape[0]     
        for feature in features:
            # take 0 and 1 for each category in feature and then compute more info
            statsDict[feature] = self.__df_stat(self.__dictStats(df, feature), target_dict,feature)
            logit_dict = statsDict[feature]['logit'].to_dict()
            statsDict[feature]['Gini'] = np.absolute(2 * auc(df[self.target_name],self.__change_dict(df,feature,logit_dict)) - 1)
        return statsDict

    def __compute_gini(self, logit_c,df,feature):
        """ method for computing gini index
        """
        ld = logit_c.to_dict()
        return np.absolute(2 * auc(df[self.target_name],self.__change_dict(df,feature,ld)) - 1)

    def __preselection(self, features, min_gini=MIN_GINI, delta_gini=DELTA_GINI):
        """Preselection of features by gini and AR_DIFF value """
        # 1. gini na kolumnie - drop < mini_gini
        results = []
        rejected_low_gini = []
        rejected_delta_gini = []
        if self.target_name in features:
            features.remove(self.target_name)
        for feature in features:
            print(feature)
            gini  = self.__compute_gini(self.stats_[feature]['logit'],self.trainBin_, feature)
            if  gini > min_gini:
                # 2. procentowa miedzy testem a treningiem  |g_train - g_test|/g_train > delta gini
                gini_test = self.__compute_gini(self.stats_[feature]['logit'],self.testBin_,feature)
                AR_Diff = self.__AR_value(gini,gini_test)
                if AR_Diff < delta_gini:
                    results.append(feature)
                else:
                    rejected_delta_gini.append([feature, AR_Diff])
            else:
                rejected_low_gini.append(
                    [feature, gini])
        return results, rejected_low_gini, rejected_delta_gini
    
    def __AR_value(self,train,test):
        '''compute AR diff value '''
        return np.absolute((train-test))/train

    def __logit_value(self,df, stats):
        '''helper method 
        change all values in columns with corresponding logit value
        '''
        logit = df.copy()
        if self.target_name in list(logit):
            logit = logit.drop(self.target_name, axis=1)
        for el in logit:
            logit[el] = self.__change_dict(logit,el,stats[el]['logit'].to_dict())
        return logit
    
    def __change_dict(self,df,feature,dict_):
        '''helper method
        map all elements for feature column'''
        return df[feature].map(dict_)

    def __selection(self, df, selector=SELECT_METHOD, n=NUM_OF_FEATURES):
        """Method for selecting best n features with chosen estimator (logistic regression as default)"""
        return self.__choose_n_best(list(df), self.__ranking_features(df, selector), n)

    def __ranking_features(self, df, selector):
        '''RFE feautre ranking from RFE selection '''
        from sklearn.feature_selection import RFE
        rfe = RFE(estimator=selector, n_features_to_select=1, step=1)
        rfe.fit(df, self.train_[self.target_name])
        return rfe.ranking_

    def __choose_n_best(self, features, ranking, n):
        '''choose n best features from ranking list'''
        result = list(ranking <= n)
        selected_features = [features[i]
                             for i, val in enumerate(result) if val == 1]
        return selected_features

    def __get_model_info(self, X, y, X_test,y_test):
        lre = LogisticRegressionCV()
        features = list(X)
        result = {"coef": {},
                  "p_value":{},
                  "features": features,
                  'model': str(lre).split("(")[0],
                  'gini': 0,
                  'acc': 0,
                  'Precision':0,
                  'Recall':0,
                  'F1':0}
        lre.fit(X, y)
        pred = lre.predict(X_test)
        p_va = stats.coef_pval(lre,X,y)
        result['acc'] = accuracy_score(y_test,pred) # accuracy classification score
        result['Precision']=precision_score(y_test,pred) # precision tp/(tp+fp) PPV
        result['Recall'] =  recall_score(y_test,pred) # Recall tp/(tp+fn) NPV
        result['F1'] = f1_score(y_test,pred) # balanced F-score weighted harmonic mean of the precision and recall
        for ix, el in enumerate(lre.coef_[0]):
            result['coef'][features[ix]] = el
            result['p_value'][features[ix]] = p_va[ix] 
        result['intercept'] = lre.intercept_
        partial_score = np.asarray(X) * lre.coef_
        for_gini_score = [sum(i) for i in partial_score] + lre.intercept_
        result['gini'] = np.absolute(2 * auc(y, for_gini_score) - 1)

        return lre, result

    def __scorecard_dict(self,features, stats, coef, inter):
        '''scorecard dictionary with score points for all categories
        with beta coefficients > 0.

        Parameters
        ----------
        features: list, list of all modeled features
        stats:    dict, dictionary with statistics
        coef:     dict, dictionary with all models coefficient
        inter:    list, list with model intercept value.

        Return
        ------
        scorecarf: dict

        '''
        alpha = inter[0]
        factor = 20/np.log(2)
        score_dict = {"variable": [], "label": [],
                      "logit": [], 'score': []}
        stats_copy = {}
        v = len(features)
        alp = 0
        # del all features with negative beta coefficient
        for el in features:
            if coef[el]<0:
                features.remove(el)
        self._scored_features_ = features        
        for el in features:
            stats_copy[el] = stats[el].sort_values(
                by='logit', ascending=False).reset_index(drop=True)
            alp += coef[el]*stats_copy[el]["logit"][0]*factor    
        alp = -alp+300
        for el in features:
            f_beta = coef[el]*stats_copy[el]["logit"][0]
            for ix, ele in enumerate(stats_copy[el]['var']):
                score_dict["variable"].append(ele)
                score_dict["label"].append(stats_copy[el]['label'][ix])
                score_dict["logit"].append(stats_copy[el]["logit"][ix])
                a1 = -(coef[el]*stats_copy[el]["logit"][ix]-f_beta + alpha/v)*factor
                a2 = alp/v
                score_dict["score"].append(int(round(a1+a2)))
            
        if score_dict["score"][0]<0:
            score_dict['score']+=np.absolute(score_dict['score'][0])+1
                           
        return score_dict
    
    def test_gini(self):
        """Compute gini for test dataset"""
        df_bin_test = self.testBin_[self._scored_features_]
        df = pd.DataFrame()
        # change bin value to score value
        for feature in list(df_bin_test):
            # get score values for beans
            df_a = self.show_stats(feature,bin_lab=True).sort_values(by="bin_label").reset_index(drop=True)
            score_dict = df_a.to_dict()['score']
            df[feature] = self.__change_dict(df_bin_test,feature,score_dict)
        df['total_score'] = (df.sum(axis=1)).astype('int')    
        X = df['total_score'].values.reshape(-1, 1)
        y = self.testBin_[self.target_name]
        gini = np.absolute(2*auc(y,X)-1)

        return gini    
    
    def __summary_features(self, features):
        summary= ""
        for feature in features:
            table = self.show_stats(feature).to_html()\
            .replace('<table border="1" class="dataframe">','<table class="table table-striped">')
            element = '<h3>'+str(feature)+'</h3>'+table
            summary += element
        return summary

    def __summary_report(self):
        all_train = self.train_.shape[0]
        all_test = self.test_.shape[0]
        train_good =self.train_[self.target_name].value_counts()[0]
        train_bad =self.train_[self.target_name].value_counts()[1]
        test_good =self.test_[self.target_name].value_counts()[0]
        test_bad =self.test_[self.target_name].value_counts()[1]
        info = {'n observed':[all_train,all_test],
                'n good':[train_good,test_good],
                'n bad':[train_bad, test_bad],
                'Percent of good [%]':[round(train_good/all_train,3)*100, round(test_good/all_test,3)*100],
                'Percent of bad [%]':[round(train_bad/all_train,3)*100, round(test_bad/all_test,3)*100]
        } 
        df = pd.DataFrame(info, index=['Training','Test'])
        summary = df[['n observed','n good','n bad', 'Percent of good [%]', 'Percent of bad [%]']].to_html()\
        .replace('<table border="1" class="dataframe">','<table class="table table-striped">')
        return summary
    
    def __model_report(self):
        summary= self.get_scorecard().to_html()\
        .replace('<table border="1" class="dataframe">','<table class="table table-striped">')
        return summary

    def __gini_report(self):
        info = {'Gini train':self.gini_model(),'Gini test':self.test_gini()}
        df = pd.DataFrame(info, index = [0])
        summary = df.to_html()\
        .replace('<table border="1" class="dataframe">','<table class="table table-striped">')
        return summary

        
    def html_report(self, name='report.html', features=None):
        if not features:
            features = self._scored_features_
        html_page = '''<!DOCTYPE html>
        <html>
            <head>
            <meta charset="utf-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <meta name="description" content="Advanced Scorecard Builder Report">
            <meta name="author" content="Sebastian Zając">
            <title>Report</title>
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
            <style>
            h2{text-align:center}</style>
            <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
            <!--[if lt IE 9]>
            <script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
            <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
            <![endif]-->
            </head>
            <body>
            <div class="jumbotron"><div class="container">
            <div class="text-center">
            <img src="https://amainstitute.pl/wp-content/uploads/2018/06/ama_logo.png" alt='AMA Instistute Logo'>
            </div>
            <h2>Advanced Scorecard Builder</h2>
            <h2>Report</h2>
            </div></div>
            <div class="container">
            <h2>Data Summary</h2><div class="summary table-responsive">'''+self.__summary_report() +'''</div>
            </div>
            <div class="container">
            <h2>Features report</h2><div class="features table-responsive">''' + self.__summary_features(features) + '''</div>
            </div><div class="container">
            <h2>Scorecard</h2><div class="score table-responsive">'''+self.__model_report()+'''</div>
            <h2>Gini</h2><div class="gini table-responsive">'''+self.__gini_report() + '''</div>
            <footer>
                <p>&copy; 2018 AMA Institute. Advanced Scorecard Builder Free Version</p>
            </footer>
            </div>
            <!-- Bootstrap core JavaScript
            ================================================== -->
            <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
            <script>$(".summary thead th:first-child").text("Set"); $(".features th:first-child, .score th:first-child, .gini th:first-child").remove()</script>
            </body>
        </html>'''
        f = open(name,'w')
        f.write(html_page)
        f.close()
        

    def get_scorecard(self):
        if hasattr(self, '_scorecard_'):
            lista = ['label', 'variable', 'score']
            return self._scorecard_[lista]
        raise Exception(ERR_SCORECARD)

    def gini_model(self):
        if hasattr(self, 'model_info_'):
            return self.model_info_['gini']
        raise Exception(ERR_GINI_MODEL)  

    def show_stats(self,name,set_name='train', bin_lab=None):
        """ Interface method for feature statistics view as DataFrame
        Parameters
        ----------
        name: string, feature names
        set_name: string, (default=train) choose train/test

        Return
        ----------
        result:   DataFrame
        """
        lista = ['label','Bad rate [%]','Percent of population [%]','n_good','n_bad',"IV"]
        if bin_lab:
            lista.append('bin_label')
            
        if set_name == 'train':
            r_part = self.stats_[name].sort_values(
                by='logit', ascending=False).reset_index(drop=True)
      
        elif set_name == 'test':
            r_part = self.stats_test_[name].sort_values(
                by='logit', ascending=False).reset_index(drop=True)           
        else:
            raise Exception('Choose train or test')
        if name in self.model_info_['features'] and self.model_info_['coef'][name]>0:
            lista = ['score','label','Bad rate [%]','Percent of population [%]','n_good','n_bad',"IV"]
            if bin_lab:
                lista.append('bin_label')   
            s_part = self._scorecard_[self._scorecard_['variable']==name][['score']].reset_index(drop=True)
            result = pd.concat([r_part,s_part],axis=1,join='inner')
        else:
            result = r_part
        return result[lista]              

