import React, { Component } from "react";
import Burger from "../../Burger/Burger";
import Button from "../../UI/Button/Button";
import classes from "./CheckOutSummary.module.css";
class CheckOutSummary extends Component {
	render() {
		return (
			<div className={classes.CheckOutSummary}>
				<h1 style={{ color: "#245", padding: "8px", border: "1px solid #FDE" }}>
					Your Order
				</h1>
				<h2 style={{ color: "#245", padding: "4px" }}>
					Price: {this.props.price} $
				</h2>
				<Burger ingredients={this.props.ingredients}></Burger>
				<div className={classes.Controls}>
					<Button btnType="Danger" clicked={this.props.cancel}>
						CANCEL
					</Button>
					<Button btnType="Success" clicked={this.props.continue}>
						CONTINUE
					</Button>
				</div>
			</div>
		);
	}
}

export default CheckOutSummary;
