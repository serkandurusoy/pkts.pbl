import { Mongo } from 'meteor/mongo';

export const Messages = new Mongo.Collection('messages');

Messages.attachSchema(new SimpleSchema({
  message: {
    type: String,
  },
  timestamp: {
    type: Date,
    defaultValue: new Date(),
    index: -1,
  },
}));
