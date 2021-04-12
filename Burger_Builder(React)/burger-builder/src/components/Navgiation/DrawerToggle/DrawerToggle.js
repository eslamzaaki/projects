import React from "react";
import classes from "./DrawerToggle.module.css";

const DrawerToggle = (props) => {
	return (
		<main className={classes.DrawerTogglee} onClick={props.clicked}>
			<div className={classes.Bar}></div>
			<div className={classes.Bar}></div>
			<div className={classes.Bar}></div>
		</main>
	);
};

export default DrawerToggle;
