import React from "react";
import NavigationItem from "../NavigationItem/NavigationItem";
import classes from "./NavigationItems.module.css";
const NavigationItems = (props) => {
	let ItemsClasses = [classes.NavigationItems];
	if (props.SideDrawer) {
		ItemsClasses = [classes.NavigationItems, classes.SideDrawer];
	}
	return (
		<ul className={ItemsClasses.join(" ")}>
			<NavigationItem link="/" exact>
				Burger Builder
			</NavigationItem>
			<NavigationItem link="/orders"> Orders</NavigationItem>
		</ul>
	);
};

export default NavigationItems;
