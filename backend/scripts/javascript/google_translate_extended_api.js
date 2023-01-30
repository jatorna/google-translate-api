
var args = process.argv

const translate = require('google-translate-extended-api');

translate.defaultDataOptions.returnRawResponse = false;
translate.defaultDataOptions.detailedTranslations = true;
translate.defaultDataOptions.definitionSynonyms = true;
translate.defaultDataOptions.detailedTranslationsSynonyms = true;
translate.defaultDataOptions.definitions = true;
translate.defaultDataOptions.definitionExamples = false;
translate.defaultDataOptions.examples = false;
translate.defaultDataOptions.removeStyles = true;

translate(args[2], args[3], args[4]).then((res) => {
    console.log(JSON.stringify(res, undefined, 2));
}).catch(console.log);
