import React from "react";
import classes from "./Input.module.css";

function Input(props) {
	let inputElement = null;
	let inputClasses = [classes.inputElement];
	if (!props.valid && props.touched) {
		inputClasses.push(classes.notValid);
	} else {
		inputClasses = [classes.in];
	}
	switch (props.elementType) {
		case "input":
			inputElement = (
				<input
					onChange={props.changed}
					{...props.elementConfig}
					value={props.value}
					className={inputClasses.join(" ")}
				></input>
			);
			break;
		case "textarea":
			inputElement = (
				<textarea
					onChange={props.changed}
					{...props.elementConfig}
					value={props.value}
					className={inputClasses.join(" ")}
				></textarea>
			);
			break;
		case "select":
			inputElement = (
				<select
					className={inputClasses.join(" ")}
					value={props.value}
					onChange={props.changed}
				>
					{props.elementConfig.options.map((option) => {
						return (
							<option value={option.vlaue} key={option.value}>
								{option.displayValue}
							</option>
						);
					})}
				</select>
			);
			break;
		default:
			inputElement = (
				<input
					onChange={props.changed}
					{...props.elementConfig}
					value={props.value}
					className={classes.InputElement}
				></input>
			);
			break;
	}
	return (
		<div className={classes.Input}>
			<label className={classes.Label}>{props.label}</label>
			{inputElement}
		</div>
	);
}

export default Input;
