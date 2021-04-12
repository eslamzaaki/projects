import React from "react";
import Logo from "../../Logo/Logo";
import DrawerToggle from "../DrawerToggle/DrawerToggle";
import NavigationItems from "../NavigationItems/NavigationItems";
import classes from "./Toolbar.module.css";
const Toolbar = (props) => {
	return (
		<header className={classes.Toolbar}>
			<DrawerToggle clicked={props.openSide}></DrawerToggle>
			<Logo height="80%"></Logo>
			<nav className={classes.DesktopOnly}>
				<NavigationItems></NavigationItems>
			</nav>
		</header>
	);
};

export default Toolbar;
