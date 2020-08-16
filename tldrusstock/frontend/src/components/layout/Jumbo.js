import React, { Component } from 'react';
// import './Jumbo.css';

export class Jumbo extends Component {
  render() {
    return (
      <div className="container pt-4 pb-2">
        <h1 className="display-4">tl;dr us stock</h1>
        <p className="lead">This shows price data of your stocks and their sentiment from latest 100 tweets.</p>
        <hr className="my-4"></hr>
      </div>
    )
  }
}

export default Jumbo
