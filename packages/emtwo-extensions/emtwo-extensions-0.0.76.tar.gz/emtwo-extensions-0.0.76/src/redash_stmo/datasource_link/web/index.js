import template from './datasource-link.html';

function controller($scope, $route) {
  const dataSources = $route.current.locals.dataSources;
  const query = $route.current.locals.query;
  $scope.dataSource = dataSources.filter(ds => ds.id === query.data_source_id);
}

export default function init(ngModule) {
  ngModule.component('datasourceLink', {
    template,
    controller,
  });
}
