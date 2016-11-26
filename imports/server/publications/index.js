import { Meteor } from 'meteor/meteor';
import { Messages } from '/imports/api';

Meteor.publish('messages', function() {
  return Messages.find();
});
