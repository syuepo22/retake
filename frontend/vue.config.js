const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  outputDir: '../registration/static/frontend/',
  indexPath: '../../templates/frontend/index.html',
  publicPath: process.env.NODE_ENV === 'production'
    ? '/static/frontend/'
    : '/'
})