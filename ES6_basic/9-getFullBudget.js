export default function getFullBudgetObject(income, gdp, capita) {
  return {
    income,
    gdp,
    capita,
    getIncomeInDollars(value) {
      return `$${value}`;
    },
    getIncomeInEuros(value) {
      return `${value} euros`;
    },
  };
}
