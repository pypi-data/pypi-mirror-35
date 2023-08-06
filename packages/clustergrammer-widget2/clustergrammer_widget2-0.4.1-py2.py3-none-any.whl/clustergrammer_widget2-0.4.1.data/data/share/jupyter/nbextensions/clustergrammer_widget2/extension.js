// Entry point for the notebook bundle containing custom model definitions.
//
// Setup notebook base URL
//
// Some static assets may be required by the custom widget javascript. The base
// url for the notebook is not known at build time and is therefore computed
// dynamically.
__webpack_public_path__ = document.querySelector('body').getAttribute('data-base-url') + 'nbextensions/clustergrammer_widget2';


define(function() {
    "use strict";

    window['requirejs'].config({
        map: {
            '*': {
                'clustergrammer_widget2': 'nbextensions/clustergrammer_widget2/index',
            },
        }
    });
    // Export the required load_ipython_extention
    return {
        load_ipython_extension : function() {}
    };
});
