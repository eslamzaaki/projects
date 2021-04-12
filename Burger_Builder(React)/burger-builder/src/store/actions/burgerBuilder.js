import * as actionTypes from "../actions/actionTypes";
import axios from "../../axios-orders";

export const addIng = (ingName) => {
	return {
		type: actionTypes.ADDING,
		ingName: ingName,
	};
};
export const removeIng = (ingName) => {
	return {
		type: actionTypes.REMOVEING,
		ingName: ingName,
	};
};
export const setIngs = (ings) => {
	return {
		type: actionTypes.RETRIVE,
		ings: ings,
	};
};
export const errorIngs = () => {
	return {
		type: actionTypes.ERRORRETRIVE,
	};
};
export const initIngs = () => {
	return (dispatch) => {
		axios
			.get("/ingredients.json")
			.then((res) => {
				dispatch(setIngs(res.data));
			})
			.catch((err) => {
				dispatch(errorIngs());
			});
	};
};
