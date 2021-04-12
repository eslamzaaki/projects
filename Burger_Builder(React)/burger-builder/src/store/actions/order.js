import * as actionTypes from "./actionTypes";
import axios from "../../axios-orders";
export const orderNow = (id, orderData) => {
	return {
		type: actionTypes.ORDER,
		id: id,
		orderData: orderData,
	};
};
export const orderFail = (e) => {
	return {
		type: actionTypes.ORDERERROR,
		error: e,
	};
};
export const asyncOrderNow = (orderData) => {
	return (dispatch) => {
		axios
			.post("/orders.json", orderData)
			.then((res) => {
				dispatch(orderNow(res.data, orderData));
			})
			.catch((error) => {
				dispatch(orderFail(error));
			});
	};
};
