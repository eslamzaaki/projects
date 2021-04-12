import React from "react";
import BuildControl from "./BuildControl/BuildControl";
import classes from "./BuildControls.module.css";

const BuildControls = (props) => {
	const controls = [
		{ label: "Meat", type: "meat" },
		{ label: "Cheese", type: "cheese" },
		{ label: "Salad", type: "salad" },
		{ label: "Bacon", type: "bacon" },
	];
	return (
		<div className={classes.BuildControls}>
			<p>
				<strong>Current Price:{props.price} $</strong>
			</p>
			{controls.map((ctrl) => {
				return (
					<BuildControl
						label={ctrl.label}
						key={ctrl.label}
						type={ctrl.type}
						disableIngs={props.disableIngs}
					></BuildControl>
				);
			})}
			<button
				className={classes.OrderButton}
				disabled={!props.purchasable}
				onClick={props.purchasing}
			>
				ORDER NOW{" "}
			</button>
		</div>
	);
};

export default BuildControls;
