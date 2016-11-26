import { Meteor } from 'meteor/meteor';
import React from 'react';
import { createContainer } from 'meteor/react-meteor-data';
import { Messages } from '/imports/api';
import moment from 'moment-timezone';

const MessagesListComponent = (props) => {
  const {
    subscriptionLoading,
    messages,
  } = props;

  if (subscriptionLoading) {
    return <div>Messages are loading...</div>
  }

  if (!messages.length) {
    return <div>There is no message in the database</div>
  }

  window.messages = messages;

  return (
    <ul>
      {messages.map(({timestamp,message},ix) => <li key={ix}><strong>{moment(timestamp).format('DD.MM.YYYY HH:mm:ss')}: </strong>{message}</li>)}
    </ul>
  );

}

export default createContainer((props) => {

  const subscription = Meteor.subscribe('messages');
  const subscriptionLoading = !subscription.ready();

  let messages;

  if (!subscriptionLoading) {
    messages = Messages.find({},{
      sort: {
        timestamp: -1,
      }
    }).fetch();
  }

  return {
    subscriptionLoading,
    messages: messages || [],
  };
}, MessagesListComponent);
