import * as actionTypes from "../actions/actionTypes";
const initialState = {
	orders: [],
	loading: false,
};

export default (state = initialState, action) => {
	switch (action.type) {
		case actionTypes.ORDER:
			return {
				...state,
				loading: false,
				orders: state.orders.concat({
					...action.orderData,
					id: action.id,
				}),
			};
		case actionTypes.ORDERERROR:
			return {
				...state,
				loading: false,
			};

		default:
			return state;
	}
};
