import React, { Component } from "react";
import Button from "../../../components/UI/Button/Button";
import Spinner from "../../../components/UI/Spinner/Spinner";
import axios from "../../../axios-orders";
import classes from "./ContactData.module.css";
import withErrorHandler from "../../../hoc/WithErrorHandler/WithErrorHandler";
import Input from "../../../components/UI/Input/Input";
import { connect } from "react-redux";
import * as orderActionCreators from "../../../store/actions/order";
class ContactData extends Component {
	state = {
		loading: false,
		formValid: false,
		orderForm: {
			name: {
				elementType: "input",
				elementConfig: {
					type: "text",
					placeholder: "Your Name",
				},
				value: "",
				validation: { required: true },
				valid: false,
				touched: false,
			},
			street: {
				elementType: "input",
				elementConfig: {
					type: "text",
					placeholder: "Street",
				},
				value: "",
				validation: { required: true },
				valid: false,
				touched: false,
			},
			zipCode: {
				elementType: "input",
				elementConfig: {
					type: "text",
					placeholder: "ZIP Code",
				},
				value: "",
				validation: { required: true, minLength: 3, maxLength: 10 },
				valid: false,
				touched: false,
			},
			country: {
				elementType: "input",
				elementConfig: {
					type: "text",
					placeholder: "Country",
				},
				value: "",
				validation: { required: false },
				valid: false,
				touched: false,
			},
			email: {
				elementType: "input",
				elementConfig: {
					type: "email",
					placeholder: "Your E-Mail",
				},
				value: "",
				validation: { required: true },
				valid: false,
				touched: false,
			},
			deliveryMethod: {
				elementType: "select",
				elementConfig: {
					options: [
						{ value: "fastest", displayValue: "Fastest" },
						{ value: "cheapest", displayValue: "Cheapest" },
					],
				},
				value: "fastest",
				validation: {},
				valid: true,
				touched: false,
			},
		},
	};
	orderHandler = (e) => {
		e.preventDefault();
		this.setState({ loading: true });
		const order = {
			ingredients: this.props.ingredients,
			price: this.props.price,
			formData: this.state.orderForm,
		};
		this.props.orderNow(order);
	};
	checkValidty = (value, validation) => {
		var isvalid = true;
		if (validation.required) {
			isvalid = value.trim() !== "";
		}
		if (validation.minLength && isvalid) {
			isvalid = value.length >= validation.minLength;
		}
		if (validation.maxLength && isvalid) {
			isvalid = value.length <= validation.maxLength;
		}
		return isvalid;
	};
	changeInputHandler = (event, identifier) => {
		const orderForm = { ...this.state.orderForm };
		const elementForm = { ...orderForm[identifier] };
		elementForm.value = event.target.value;
		elementForm.valid = this.checkValidty(
			event.target.value,
			elementForm.validation
		);
		let formValid = true;
		for (let element in orderForm) {
			formValid = orderForm[element].valid && formValid;
		}
		elementForm.touched = true;
		orderForm[identifier] = elementForm;
		this.setState({
			orderForm: orderForm,
			formValid: formValid,
		});
	};
	render() {
		let orderArray = [];
		for (let key in this.state.orderForm) {
			orderArray.push({ id: key, config: this.state.orderForm[key] });
		}
		// [{street:{type,config,vlaue}},...]
		let form = (
			<form onSubmit={this.orderHandler}>
				{orderArray.map((element) => {
					return (
						<Input
							elementType={element.config.elementType}
							elementConfig={element.config.elementConfig}
							value={element.config.value}
							key={element.id}
							touched={element.config.touched}
							valid={element.config.valid}
							changed={(event) => {
								this.changeInputHandler(event, element.id);
							}}
							disabled={this.state.formValid}
						></Input>
					);
				})}
				<Button btnType="Success" disabled={!this.state.formValid}>
					Order
				</Button>
			</form>
		);
		if (this.state.loading) {
			form = <Spinner></Spinner>;
		}
		return (
			<div className={classes.ContactData}>
				<h2 style={{ marginBottom: "6px" }}>Enter contact data</h2>
				{form}
			</div>
		);
	}
}
const mapActionToProps = (dispatch) => {
	return {
		orderNow: (orderData) => {
			orderActionCreators(orderData);
		},
	};
};
const mapStateToProps = (state) => {
	return {
		ingredients: state.ingredients,
		price: state.totalPrice,
	};
};

export default connect(
	mapStateToProps,
	mapActionToProps
)(withErrorHandler(ContactData, axios));
