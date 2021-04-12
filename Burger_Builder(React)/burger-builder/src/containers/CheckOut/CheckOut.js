import classes from "./CheckOut.module.css";
import React, { Component } from "react";
import { Route } from "react-router";
import CheckOutSummary from "../../components/Order/CheckOutSummary/CheckOutSummary";
import ContactData from "./ContactData/ContactData";
import { connect } from "react-redux";

class CheckOut extends Component {
	cancelCheckout = () => {
		this.props.history.goBack();
	};
	continueCheckout = () => {
		this.props.history.replace("/checkout/contact-data");
	};

	render() {
		return (
			<div className={classes.CheckOut}>
				<CheckOutSummary
					cancel={this.cancelCheckout}
					continue={this.continueCheckout}
					ingredients={this.props.ings}
					price={this.props.price}
				></CheckOutSummary>
				<Route path="/checkout/contact-data" component={ContactData} />
			</div>
		);
	}
}
const mapStateToProps = (state) => {
	return { ings: state.ingredients, price: state.totalPrice };
};
export default connect(mapStateToProps)(CheckOut);
