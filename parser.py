import csv

class BankParser:
        # The type of currency transactions need to conform to
        CURRENCY_TYPE = "EUR"

        # Array with all (part of) descriptions that are about groceries
        GROCERY_TRANSACTION_CLASSIFICATIONS = ["Albert Heijn", 
                                                "AH to go", 
                                                "AH Ksk", 
                                                "ah kiosk", 
                                                "Starbucks", 
                                                "ASA BK",
                                                "Dekamarkt",
                                                "AH Station",
                                                "Doner Company",
                                                "DIRCKIII",
                                                "DIRK VDBROEK",
                                                "MCDONALDS",
                                                "Lidl"]

        # Array with all (part of) descriptions that are about sports
        SPORT_TRANSACTION_CLASSIFICATIONS = ["Sportexpl.UvA", "Sloterparkbad"]

        totalCredit = 0
        totalDebit = 0
        difference = 0

        totalGroceries = 0
        totalSports = 0
        totalOVChipkaart = 0
        totalZorgToeslag = 0
        totalHuurToeslag = 0
        totalStudieFinanciering = 0
        totalCollegeGeld = 0
        totalPayPal = 0

        totalCreditDebit = 0
        totalAmountClassified = 0
        totalAmountNotClassified = 0

        def parse(self):
                # Parse file
                with open('transacties.txt', 'rb') as csvfile:
                        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
                        for row in reader:
                                # Parse data
                                fromAccount = row[0]
                                currency = row[1]
                                interestDate = row[2]
                                transactionType = row[3]
                                amount = float(row[4])
                                toAccount = row[5]
                                accountName = row[6]
                                processDate = row[7]
                                transactionTypeDetailed = row[8]
                                descriptionLine1 = row[10]
                                descriptionLine2 = row[11]
                                descriptionLine3 = row[12]
                                descriptionLine4 = row[13]
                                description = descriptionLine1 + descriptionLine2 + descriptionLine3 +  descriptionLine4

                                # Make sure we are in the same currency
                                if currency != self.CURRENCY_TYPE:
                                        raise Exception("Foreign currency detected.")

                                # Calculate debit and credit
                                if transactionType == "C":
                                        self.totalCredit += amount
                                elif transactionType == "D":
                                        self.totalDebit += amount
                                else:
                                        raise Exception("Unknown Transaction Type")

                                # Start classifying
                                self.classify(transactionType, description, accountName, amount)


                # Finish totals
                self.difference =  self.totalCredit - self.totalDebit
                self.totalCreditDebit = self.totalCredit + self.totalDebit
                self.totalAmountClassified = self.totalGroceries + self.totalSports + self.totalOVChipkaart + self.totalZorgToeslag + self.totalHuurToeslag + self.totalStudieFinanciering + self.totalCollegeGeld + self.totalPayPal
                self.totalAmountNotClassified = self.totalCreditDebit - self.totalAmountClassified

                # Report values
                print self.report()

        # Get dictionary with all values
        def report(self):

                output = {"total_credit_debit": self.totalCreditDebit,
                        "total_credit": self.totalCredit,
                        "total_debit": self.totalDebit,
                        "difference": self.difference,
                        "amount_classified": self.totalAmountClassified,
                        "amount_not_classified": self.totalAmountNotClassified,
                        "credit": {
                                "zorg_toeslag": self.totalZorgToeslag,
                                "huur_toeslag": self.totalHuurToeslag,
                                "studiefinanciering": self.totalStudieFinanciering,
                        },
                        "debit": {
                                "groceries": self.totalGroceries,
                                "sport": self.totalSports,
                                "ov_chipkaart": self.totalOVChipkaart,
                                "collegegeld": self.totalCollegeGeld,
                                "paypal": self.totalPayPal,
                        }
                }
                return output


        # Classifies transaction
        def classify(self, transactionType, description, accountName, amount):
                # Classify Groceries
                if transactionType == "D":
                        for classification in self.GROCERY_TRANSACTION_CLASSIFICATIONS:
                                if classification in description:
                                        self.totalGroceries += amount
                                        return

                # Classify Sports
                if transactionType == "D":
                        for classification in self.SPORT_TRANSACTION_CLASSIFICATIONS:
                                if classification in description:
                                        self.totalSports += amount
                                        return

                # Classify OV Chipkaart
                if transactionType == "D":
                        if "OV-chipkaart" in description:
                                self.totalOVChipkaart += amount
                                return

                # Classify Zorg Toeslag
                if transactionType == "C":
                        if "ZORGTOESLAG" in description:
                                self.totalZorgToeslag += amount
                                return

                # Classify Huur Toeslag
                if transactionType == "C":
                        if "HUURTOESLAG" in description:
                                self.totalHuurToeslag += amount
                                return

                # Classify Studiefinanciering
                if transactionType == "C":
                        if "DUO" in accountName:
                                self.totalStudieFinanciering += amount
                                return

                # Classify College geld
                if transactionType == "D":
                        if "Incasso collegegeld" in description:
                                self.totalCollegeGeld += amount
                                return

                # Classify PayPal
                if transactionType == "D":
                        if "PayPal" in accountName:
                                self.totalPayPal += amount
                                return


if __name__ == "__main__":
        BankParser().parse()
        
