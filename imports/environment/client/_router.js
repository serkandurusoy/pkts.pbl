import { Meteor } from 'meteor/meteor';
import React  from 'react';
import { render } from 'react-dom';
import { App } from '/imports/client/ui/layouts';
import {
  Router,
  Route,
  browserHistory,
} from 'react-router';

Meteor.startup(() => {
  render(
    <Router history={browserHistory}>
      <Route path="/" component={App} />
    </Router>
    ,
    document.getElementById('root')
  );
});
