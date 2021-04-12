import React, { Component } from "react";
import classes from "./BuildControl.module.css";
import { connect } from "react-redux";
import * as burgerActionCreators from "../../../../store/actions/burgerBuilder";
class BuildControl extends Component {
	render() {
		return (
			<div className={classes.BuildControl}>
				<div className={classes.Label}>{this.props.label}</div>
				<button
					className={classes.Less}
					onClick={() => {
						this.props.onClickREMOVE(this.props.type);
					}}
					disabled={this.props.disableIngs[this.props.type]}
				>
					less
				</button>
				<button
					className={classes.More}
					onClick={() => {
						this.props.onClickADD(this.props.type);
					}}
				>
					More
				</button>
			</div>
		);
	}
}

const mapDispatchToProps = (dispatch) => {
	return {
		onClickADD: (ingName) => dispatch(burgerActionCreators.addIng(ingName)),
		onClickREMOVE: (ingName) =>
			dispatch(burgerActionCreators.removeIng(ingName)),
	};
};
export default connect(null, mapDispatchToProps)(BuildControl);
