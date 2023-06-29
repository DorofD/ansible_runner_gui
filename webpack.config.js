const path = require('path');

module.exports = {
    // Здесь указываем, какой файл считать главным.
    entry: './static/js/dev.js',
    // Скомпилированный бандл положим под именем main.js.
    output: {
      path: path.resolve(__dirname, 'static/js'),
      filename: "main.js"
    },
    module: {
      rules: [
      // Здесь мы будем описывать правила трансформаций, которые будут
      // применяться к файлам различного типа.
      ]
    },
    // Здесь мы применим различные плагины, расширяющие возможности Webpack
    plugins: [
    ]
  }; 