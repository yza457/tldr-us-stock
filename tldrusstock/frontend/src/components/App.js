import React, { Component } from 'react';
import ReactDOM from 'react-dom';

import Header from './layout/Header'
import Jumbo from './layout/Jumbo'
import Loading from './layout/Loading'
import Input from './input/Input'
import CardList from './cardlist/CardList'

const initialState = {
  input: "",
  loading: false,
  stocks: "",
  // a list of stock and their information
  stockList: []
}

class App extends Component {
  constructor() {
    super();
    this.state = initialState;
  }

  onInputChange = (event) => {
    this.setState({input: event.target.value });
  }

  onButtonSubmit = () => {
    console.log(this.state.input);
    this.setState({stock: this.state.input, loading: true});
    fetch('http://localhost:8000/tldr/submit', {
      method: 'post',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({
        input: this.state.input
      })
    })
    .then(response => response.json())
    .then(response =>  {
      // TODO
      this.setState({stockList : response, loading: false})
      console.log(response);
     })
    .catch(console.log);
  }

  render() {
    const {loading, stockList} = this.state;
    return (
      <div>
        <Header />
        <Jumbo />
        <Input onInputChange={this.onInputChange} onButtonSubmit={this.onButtonSubmit} />
        {loading? <Loading/> : null}
        {stockList.length === 0 || loading ? null : 
          <CardList stockList={this.state.stockList}/>
        }
      </div>
    )
  }
}

ReactDOM.render(<App />, document.getElementById('app'));
