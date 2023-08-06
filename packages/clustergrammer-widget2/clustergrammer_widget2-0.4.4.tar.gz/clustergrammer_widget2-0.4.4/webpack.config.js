// Custom webpack rules
const rules = [
  { test: /\.ts$/, loader: 'ts-loader' },
  { test: /\.js$/, loader: 'source-map-loader' },
];

// Packages that shouldn't be bundled but loaded at runtime
const externals = ['@jupyter-widgets/base', 'three', 'jupyter-threejs'];
var version = require('./package.json').version;

module.exports = [
  {
    // Notebook extension
    mode:'development',
    entry: './src/index.ts',
    output: {
      filename: 'index.js',
      path: __dirname + '/clustergrammer_widget2/nbextension/static',
      libraryTarget: 'amd'
    },
    module: {
      rules: rules
    },
    devtool: 'source-map',
    externals: ['@jupyter-widgets/base'],
    resolve: {
      // Add '.ts' and '.tsx' as resolvable extensions.
      extensions: [".webpack.js", ".web.js", ".ts", ".js"]
    }
  },

  {
    // embeddable bundle (e.g. for docs)
    entry: './src/index.ts',
    output: {
      filename: 'embed-bundle.js',
      path: __dirname + '/docs/source/_static',
      library: "clustergrammer_widget2",
      libraryTarget: 'amd'
    },
    module: {
      rules: rules
    },
    devtool: 'source-map',
    externals: ['@jupyter-widgets/base'],
    resolve: {
      // Add '.ts' and '.tsx' as resolvable extensions.
      extensions: [".webpack.js", ".web.js", ".ts", ".js"]
    },
  },
  {// Embeddable {{ cookiecutter.npm_package_name }} bundle
     //
     // This bundle is generally almost identical to the notebook bundle
     // containing the custom widget views and models.
     //
     // The only difference is in the configuration of the webpack public path
     // for the static assets.
     //
     // It will be automatically distributed by unpkg to work with the static
     // widget embedder.
     //
     // The target bundle is always `dist/index.js`, which is the path required
     // by the custom widget embedder.
     //
        entry: './lib/index.js',
        output: {
            filename: 'index.js',
            // path: path.resolve(__dirname, 'dist'),
            path: __dirname + 'dist', // path.resolve(__dirname, 'dist'),
            libraryTarget: 'amd',
            // publicPath: 'https://unpkg.com/clustergrammer_widget2@' + version + '/dist/'
            publicPath: 'https://unpkg.com/clustergrammer_widget2@' + version + '/lib/'
        },
        devtool: 'source-map',
        module: {
            rules: rules
        },
        externals: ['@jupyter-widgets/base']
    }
];
