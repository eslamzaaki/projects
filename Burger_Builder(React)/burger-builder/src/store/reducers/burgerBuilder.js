import * as actionTypes from "../actions/actionTypes";
const intialState = {
	ingredients: null,
	totalPrice: 4,
	errorInitIngs: false,
};
const prices = {
	bacon: 0.5,
	cheese: 1,
	meat: 4,
	salad: 2,
};
const reducer = (state = intialState, action) => {
	switch (action.type) {
		case actionTypes.ADDING:
			return {
				...state,
				ingredients: {
					...state.ingredients,
					[action.ingName]: state.ingredients[action.ingName] + 1,
				},
				totalPrice: state.totalPrice + prices[action.ingName],
			};
		case actionTypes.REMOVEING:
			return {
				...state,
				ingredients: {
					...state.ingredients,
					[action.ingName]: state.ingredients[action.ingName] - 1,
				},
				totalPrice: state.totalPrice - prices[action.ingName],
			};
		case actionTypes.RETRIVE:
			return {
				...state,
				ingredients: { ...action.ings },
				errorInitIngs: false,
			};
		case actionTypes.ERRORRETRIVE:
			return {
				...state,
				errorInitIngs: true,
			};
		default:
			return state;
	}
};
export default reducer;
