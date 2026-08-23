module.exports = {
  env: {
    es6: true,
    node: true,
    jest: true,
  },
  extends: ['airbnb-base'],
  parserOptions: {
    ecmaVersion: 2018,
    sourceType: 'module',
  },
  rules: {
    'max-classes-per-file': 'off',
    'no-console': 'off',
    'no-underscore-dangle': 'off',
  },
};
