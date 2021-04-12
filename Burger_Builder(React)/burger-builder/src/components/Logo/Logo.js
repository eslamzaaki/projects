import React from "react";
import LogoSrc from "../../assets/images/burger-logo.png";
import classes from "./Logo.module.css";
const Logo = (props) => {
	return (
		<div className={classes.Logo} style={{ height: props.height }}>
			<img alt="BurgerHub" src={LogoSrc}></img>
		</div>
	);
};

export default Logo;
