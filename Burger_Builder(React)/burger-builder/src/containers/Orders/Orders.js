import classes from "./Orders.module.css";
import React, { Component } from "react";
import Order from "../../components/Order/Order";
import axios from "../../axios-orders";
import withErrorHandler from "../../hoc/WithErrorHandler/WithErrorHandler";
import Spinner from "../../components/UI/Spinner/Spinner";

class Orders extends Component {
	state = {
		orders: [],
		loading: true,
	};
	componentDidMount() {
		let fetchedOrders = [];
		axios
			.get("/orders.json")
			.then((res) => {
				for (let key in res.data) {
					fetchedOrders.push({
						...res.data[key],
						id: key,
					});
				}
				this.setState({ orders: fetchedOrders, loading: false });
			})
			.catch((e) => {
				console.log(e);
				this.setState({ loading: false });
			});
	}

	render() {
		var orders = <Spinner></Spinner>;
		if (!this.state.loading) {
			orders = this.state.orders.map((order) => {
				return (
					<Order
						price={order.price}
						ingredients={order.ingredients}
						key={order.id}
					></Order>
				);
			});
		}
		return <div className={classes.Orders}>{orders}</div>;
	}
}

export default withErrorHandler(Orders, axios);
