import React from "react";
import Logo from "../../Logo/Logo";
import NavigationItems from "../NavigationItems/NavigationItems";
import classes from "./SideDrawer.module.css";
import BackDrop from "../../UI/BackDrop/BackDrop";
const SideDrawer = (props) => {
	let SideClasses = [classes.SideDrawer, classes.Close];
	if (props.showSideDrawer) {
		SideClasses = [classes.SideDrawer, classes.Open];
	}
	return (
		<React.Fragment>
			<BackDrop show={props.showSideDrawer} cancel={props.closed}></BackDrop>
			<div className={SideClasses.join(" ")}>
				<Logo height="11%"></Logo>
				<nav>
					<NavigationItems SideDrawer></NavigationItems>
				</nav>
			</div>
		</React.Fragment>
	);
};

export default SideDrawer;
