
#### Instantiating Other Controller in current Controller Context.

1) Add **NameOfControllerFile.js** which needs to be instantiated in the **resolve section** of current state.

	state('xyz',{
                    url:'/test',
                    views:{
                        'index':{
                            templateUrl: '',
                            controller: 'CurrentController as Current',
                            resolve: route.resolve([NameOfControllerFile.js])
                        }
                    }
    });

2) Inject **"$controller" service** to Current Controller.

3) instantiate required controller using  **$controller(NameOfController, {$scope:$scope});**