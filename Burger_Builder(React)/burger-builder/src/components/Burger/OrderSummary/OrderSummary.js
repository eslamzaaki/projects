import React, { Component } from "react";
import Button from "../../UI/Button/Button";

class OrderSummary extends Component {
	render() {
		const ings = [];
		for (let key in this.props.ingredients) {
			ings.push(
				<li key={key}>
					{key}: {this.props.ingredients[key]}
				</li>
			);
		}
		return (
			<div>
				<h3>Great Burger with best gredients</h3>
				<ul>{ings}</ul>
				<h4>Total Price: {this.props.price}$</h4>
				<p>You want to continue ?</p>
				<Button btnType="Danger" clicked={this.props.cancel}>
					CANCEL
				</Button>
				<Button btnType="Success" clicked={this.props.continue}>
					CONTINUE
				</Button>
			</div>
		);
	}
}

export default OrderSummary;
