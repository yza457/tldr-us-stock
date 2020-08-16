import React, { Component } from 'react'

export class Loading extends Component {
  render() {
    return (
      <div className="d-flex mt-5 flex-column align-items-center justify-content-center">
        <div className="row">
            <div className="spinner-border" role="status">
                <span className="sr-only">Loading...</span>
            </div>
          </div>
          <div className="row">
            <p>Analysing..</p>
          </div>
      </div>
    )
  }
}

export default Loading
