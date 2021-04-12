import React, { Component, Fragment } from "react";
import SideDrawer from "../Navgiation/SideDrawer/SideDrawer";
import Toolbar from "../Navgiation/Toolbar/Toolbar";
import classes from "./Layout.module.css";
class Layout extends Component {
	state = {
		showSideDrawer: false,
	};
	ClosSideDrawer = () => {
		this.setState({
			showSideDrawer: false,
		});
	};
	openSideDrawer = () => {
		this.setState({
			showSideDrawer: true,
		});
	};
	render() {
		return (
			<Fragment>
				<Toolbar openSide={this.openSideDrawer}></Toolbar>
				<SideDrawer
					closed={this.ClosSideDrawer}
					showSideDrawer={this.state.showSideDrawer}
				></SideDrawer>
				<main className={classes.main}> {this.props.children} </main>
			</Fragment>
		);
	}
}

export default Layout;
