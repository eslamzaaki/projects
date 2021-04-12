import React, { Component } from "react";
import Modal from "../../components/UI/Modal/Modal";

const withErrorHandler = (WrappedComp, axios) => {
	return class extends Component {
		state = {
			error: null,
		};
		componentWillMount() {
			this.reqInt = axios.interceptors.request.use(
				(req) => {
					this.setState({ error: null });
					return req;
				},
				(error) => {
					this.setState({
						error: error,
					});
				}
			);
			this.resInt = axios.interceptors.response.use(
				(res) => {
					this.setState({ error: null });
					return res;
				},

				(error) => {
					this.setState({
						error: error,
					});
				}
			);
		}
		componentWillUnmount() {
			axios.interceptors.request.eject(this.reqInt);
			axios.interceptors.response.eject(this.resInt);
		}
		cancelErrorMessage = () => {
			this.setState({ error: null });
		};
		render() {
			return (
				<React.Fragment>
					<Modal show={this.state.error} cancel={this.cancelErrorMessage}>
						<h4 style={{ textAlign: "center" }}>
							{" "}
							{this.state.error ? this.state.error.message : null}
						</h4>
					</Modal>
					<WrappedComp {...this.props}></WrappedComp>
				</React.Fragment>
			);
		}
	};
};
export default withErrorHandler;
