import React, { Component, Fragment } from "react";
import BuildControls from "../../components/Burger/BuildControls/BuildControls";
import Burger from "../../components/Burger/Burger";
import Modal from "../../components/UI/Modal/Modal";
import OrderSummary from "../../components/Burger/OrderSummary/OrderSummary";
import axios from "../../axios-orders";
import withErrorHandler from "../../hoc/WithErrorHandler/WithErrorHandler";
import { connect } from "react-redux";
import * as burgerActionCreators from "../../store/actions/burgerBuilder";

class BurgerBuilder extends Component {
	state = {
		purchasable: false,
		purchasing: false,
	};
	continuePurchasing = () => {
		this.props.history.push({
			pathname: "/checkout",
		});
	};

	cancelPurchasing = () => {
		this.setState({ purchasing: false });
	};
	purchasingHandler = () => {
		this.setState({ purchasing: true });
	};
	sum_quantity = (ingredients) => {
		let total_quantity = 0;
		for (let key in ingredients) {
			total_quantity += ingredients[key];
		}
		return total_quantity > 0;
	};

	componentDidMount() {
		this.props.initIngs();
	}
	render() {
		let disableIngs = { ...this.props.ings };
		for (let key in disableIngs) {
			disableIngs[key] = disableIngs[key] <= 0;
		}

		if (this.props.ings) {
			var orderSummary = (
				<OrderSummary
					ingredients={this.props.ings}
					cancel={this.cancelPurchasing}
					continue={this.continuePurchasing}
					price={this.state.totalPrice}
				></OrderSummary>
			);
		}

		//intial case while ingredients retrive
		if (this.props.error) {
			var burger = (
				<div
					style={{
						fontSize: "1.5rem",
						marginTop: "50px",
					}}
				>
					can't load ingrediens
				</div>
			);
		}

		if (this.props.ings) {
			burger = (
				<Fragment>
					{" "}
					<Burger></Burger>
					<BuildControls
						price={this.props.price}
						purchasable={this.sum_quantity(this.props.ings)}
						purchasing={this.purchasingHandler}
						disableIngs={disableIngs}
					></BuildControls>
				</Fragment>
			);
		}

		return (
			<Fragment>
				<Modal show={this.state.purchasing} cancel={this.cancelPurchasing}>
					{orderSummary}
				</Modal>
				{burger}
			</Fragment>
		);
	}
}
const mapActionToProps = (dispatch) => {
	return {
		initIngs: () => {
			dispatch(burgerActionCreators.initIngs());
		},
	};
};
const mapStateToProps = (state) => {
	return {
		ings: state.ingredients,
		price: state.totalPrice,
		error: state.errorInitIngs,
	};
};

export default connect(
	mapStateToProps,
	mapActionToProps
)(withErrorHandler(BurgerBuilder, axios));
