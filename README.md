# RabobankTransactionsParser
Parses the transactions from your Rabobank account and shows an overview of your payments per category.

### What is it?
Banks aren't allowed to analyze your transactions in depth. This is good for privacy, but on the other hand bad, because you don't have insights on where your money is going to or coming from.

Instead of categorizing transactions on your own, you can now use this script to do the math for you.

This is a stripped down version of a script that I am using myself, but which ofcourse can be extended to categorize other things or to do it more in depth and more accurately.

### How can I get it to work?
1. Login to your Rabobank
2. Go to "Downloaden transacties"
3. Choose your bank accounts (I tested it with only one) and the period you are interested in. Make sure comma seperated file (.csv) is selected as file format.
4. Start the download and feed it into the script.
5. Based on the script you will see an output something like

```json
{
"credit":{
  "zorg_toeslag":10.0,
  "huur_toeslag":10.0,
  "studiefinanciering":10.0
},
"difference":10.0,
"total_debit":10.0,
"total_credit":10.0,
"amount_classified":10.0,
"amount_not_classified":10.0,
"total_credit_debit":10.0,
"debit":{
  "collegegeld":10.0,
  "paypal":10.0,
  "sport":10.0,
  "groceries":10.0,
  "ov_chipkaart":10.0
}
}
```
