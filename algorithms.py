import pickle
def decisionTree(X, y, self):
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
    from sklearn.tree import DecisionTreeClassifier
    classifier = DecisionTreeClassifier()
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)
    from sklearn.metrics import classification_report, confusion_matrix
    print(classification_report(y_test, y_pred))
    self.textBrowser_resultado.setText(classification_report(y_test, y_pred))
    with open('decision_tree_text_classifier', 'wb') as picklefile:
        pickle.dump(classifier,picklefile)
    plotAlgorithm(classifier, X_test, y_test)


def randomForest(X, y,self):
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=0)
    from sklearn.ensemble import RandomForestClassifier
    classifier = RandomForestClassifier(n_estimators=1000, random_state=0)
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)
    from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
    self.textBrowser_resultado.setText(classification_report(y_test, y_pred))
    with open('random_forest_text_classifier', 'wb') as picklefile:
        pickle.dump(classifier,picklefile)
    plotAlgorithm(classifier, X_test, y_test)


def supportVectorMachine(X, y, self):
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
    from sklearn.svm import SVC
    classifier = SVC(kernel='linear')
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)
    from sklearn.metrics import classification_report, confusion_matrix
    self.textBrowser_resultado.setText(classification_report(y_test, y_pred))
    plotAlgorithm(classifier, X_test, y_test)
    with open('svm_text_classifier', 'wb') as picklefile:
        pickle.dump(classifier,picklefile)


def plotAlgorithm(classifier, X_test, y_test):
    from sklearn.metrics import plot_confusion_matrix
    import matplotlib.pyplot as plt
    plot_confusion_matrix(classifier, X_test, y_test)
    plt.show()
