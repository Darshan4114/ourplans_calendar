import React, { Component } from "react";

import "./app.css";
import Form from "./components/Form";
import DateInfo from "./components/DateInfo";
import { DateContext } from "./context/Context";
const { Provider } = DateContext;
class App extends Component {
  state = {
    date: "",
    setDate: ({ value }) => this.setState({ date: value }),
  };
  render() {
    return (
      <div className="App">
        <Provider value={this.state}>
          <Form />
          <DateInfo />
        </Provider>
      </div>
    );
  }
}

export default App;
