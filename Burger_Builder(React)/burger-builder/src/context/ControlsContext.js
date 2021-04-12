import React from "react";
const ControlsContenxt = React.createContext({
	MoreHandler: () => {},
	LessHandler: () => {},
	disableIngs: {},
});
export default ControlsContenxt;
