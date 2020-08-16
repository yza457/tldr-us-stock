import React from 'react'

const Input = ({onInputChange, onButtonSubmit}) => {
  return (
    <div className="container">
      <div className="d-flex">
          <input placeholder='input stock tickers seperated by comma e.g. aapl, tsla' 
            className="form-control mr-1" type='tex' onChange={onInputChange}></input>
          <button className="btn btn-primary" onClick={onButtonSubmit}>enter</button>
      </div>
    </div>
  )
}

// export class Input extends Component {
//   render() {
//     return (
//     <div className="container">
//       <div className="d-flex">
//           <input placeholder='input stock tickers seperated by comma e.g. aapl, tsla' 
//             className="form-control mr-1" type='tex' onChange={onInputChange}></input>
//           <button className="btn btn-primary" onClick={onButtonSubmit}>enter</button>
//       </div>
//     </div>
//     )
//   }
// }

export default Input
