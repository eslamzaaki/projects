import React, { Component } from "react";
import BackDrop from "../BackDrop/BackDrop";
import classes from "./Modal.module.css";
class Modal extends Component {
	shouldComponentUpdate(nextProps, nextState) {
		return (
			nextProps.show !== this.props.show ||
			nextProps.children !== this.props.children
		);
	}

	componentDidUpdate() {}
	render() {
		return (
			<React.Fragment>
				<BackDrop show={this.props.show} cancel={this.props.cancel}></BackDrop>
				<div
					className={classes.Modal}
					style={{
						transform: this.props.show ? "translateY(0)" : "translateY(-100vh)",
						opacity: this.props.show ? "1" : "0",
					}}
				>
					{this.props.children}
				</div>
			</React.Fragment>
		);
	}
}

export default Modal;
