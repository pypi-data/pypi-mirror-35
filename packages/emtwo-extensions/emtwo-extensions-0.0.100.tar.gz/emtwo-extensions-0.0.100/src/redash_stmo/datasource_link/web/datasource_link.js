import React from 'react';
import PropTypes from 'prop-types';
import { react2angular } from 'react2angular';

class DatasourceLink extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      type_name: "",
      doc_url: "",
    };
  }

  componentDidMount() {
    const query = this.props.$route.current.locals.query;
    fetch(`${this.props.clientConfig.basePath}api/data_sources/${query.data_source_id}/link`)
      .then(response => { 
        if (response.status === 200) {
          return response.json();
        }
        return {};
      })
      .then(json => {
        const {type_name, doc_url} = json.message;
        this.setState({type_name, doc_url});
      });
  }

  render() {
    if (!this.state.doc_url) {
      return null;
    }
    return (
      <span id="datasource-link">
          <a href={this.state.doc_url}> {this.state.type_name} documentation</a>
      </span>
    ); 
  }
}

export default function init(ngModule) {
    ngModule.component('datasourceLink', react2angular(DatasourceLink, [], ['$route', 'clientConfig']));
}
