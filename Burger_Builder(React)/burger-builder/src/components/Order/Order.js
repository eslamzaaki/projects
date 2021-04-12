import classes from "./Order.module.css";
import React from "react";

export default function Order(props) {
	let ingArray = [];
	for (let ing in props.ingredients) {
		ingArray.push(`${ing} (${props.ingredients[ing]})`);
	}
	let ingString = ingArray.join(" - ");
	return (
		<div className={classes.Order}>
			<p>ingrediens: {ingString}</p>
			<p>
				Price: <strong>{props.price} USD</strong>
			</p>
		</div>
	);
}
