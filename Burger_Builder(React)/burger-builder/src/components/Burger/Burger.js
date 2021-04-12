import React from "react";
import BurgerIngredient from "./BurgerIng/BurgerIng";
import classes from "./Burger.module.css";
import { connect } from "react-redux";
const Burger = (props) => {
	let middleIngredients = [];
	for (let type_gredient in props.ings) {
		for (let i = 0; i < props.ings[type_gredient]; i++) {
			middleIngredients.push(
				<BurgerIngredient
					type={type_gredient}
					key={type_gredient + "" + i}
				></BurgerIngredient>
			);
		}
	}
	if (middleIngredients.length === 0) {
		middleIngredients.push(<p key="zero">Please Start add ingredients</p>);
	}
	return (
		<div className={classes.Burger}>
			<BurgerIngredient type="bread-top"></BurgerIngredient>
			{middleIngredients}
			<BurgerIngredient type="bread-bottom"></BurgerIngredient>
		</div>
	);
};
const mapStateToProps = (state) => {
	return { ings: state.ingredients };
};
export default connect(mapStateToProps)(Burger);
