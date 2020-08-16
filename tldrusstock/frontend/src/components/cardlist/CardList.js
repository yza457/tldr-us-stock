import React, { Component } from 'react'

const cardStyle = {
  minWidth: '12rem',
  maxWidth: '10rem'
};

class Card extends Component {
  render() {
    return (
      <div className="card mb-3 h-100" style={cardStyle}>
        <div className="card-body">
          <h5 className="card-title text-center">{this.props.value.name}</h5>
          <h6 className="card-subtitle mb-2 text-muted text-center">{this.props.value.ticker}</h6>
          <p className="card-text text-center">
            price : {this.props.value.price}<br />
            percent : {this.props.value.change}%<br />
            sentiment<br />
            positive : {this.props.value.positive}<br />
            negative : {this.props.value.negative}<br />
          </p>
        </div>
      </div>
    )
  }
}

class InvalidCard extends Component {
  render() {
    return (
      <div className="card mb-3 h-100" style={cardStyle}>
        <div className="card-body">
          <h5 className="card-title text-center">{this.props.value.ticker}</h5>
          <p className="card-text text-center">
            Invalid ticker, please check
          </p>
        </div>
      </div>
    )
  }
}



const CardList = ({stockList}) => {
  let cards = [];
  for (let i = 0; i < stockList.length; i++) {
    cards.push((stockList[i].error)? <InvalidCard value={stockList[i]} key={i}/> : <Card value={stockList[i]} key={i}/>);
  }

  return (
    <div className="container pt-4">
      <div className="card-deck">
        {cards}
      </div>
    </div>
  )
}

export default CardList
