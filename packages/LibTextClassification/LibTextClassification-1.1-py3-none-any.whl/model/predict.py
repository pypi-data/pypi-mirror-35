import tensorflow as tf
from os import path


class Predicter(object):

    def __init__(self, model_name, arg_dict, ckpt_dir):
        config = tf.ConfigProto()
        config.gpu_options.allow_growth = True
        self.sess = tf.Session(config=config)
        with self.sess.as_default():
            # Instantiate Model
            Model = getattr(__import__("model"), model_name)
            self.model = Model(arg_dict)
            # vocab_size = len(vocab)
            # self.averagePooling = AveragePooling(vocab_size, class_num, 0.0, 0.0,
            #                                      0.0, embed_size, sequence_len, False)
            # Initialize Save
            self.placeholder_dict = self.model.get_predict_placeholders()
            saver = tf.train.Saver()
            if path.exists(path.join(ckpt_dir, "checkpoint")):
                print("Restoring Variables from Checkpoint")
                saver.restore(self.sess, tf.train.latest_checkpoint(ckpt_dir))
            else:
                print("Can't find the checkpoint. Going to stop")
                exit(1)

    def predict(self, data, binary=False):
        # if len(text) == 0:
        #     return 0
        # input_dict = {
        #     "input_x": pad_sequences([text], maxlen=self.sequence_len, value=0.),
        #     "input_length": np.array([[len(text)]])
        # }
        feed_dict = {}
        for k in self.placeholder_dict.keys():
            try:
                feed_dict[self.placeholder_dict[k]] = data[k]
            except Exception:
                print("'%s' is acquired!", k)
                exit(1)
        feed_dict[self.model.dropout_keep_prob] = 1.0
        with self.sess.as_default():
            logits = self.sess.run(self.model.logits, feed_dict)
        if binary:
            return [float(p[0]) for p in logits]
        indices = []
        scores = []
        for logit in logits:
            li = logit.tolist()
            score = max(li)
            index = li.index(score)
            indices.append(index)
            scores.append(score)
        return indices, scores

    # def batch_predict(self, data_list):
    #     feed_dict = {}

    #     input_length = np.array([[len(text)] for text in text_list])
    #     input_x = pad_sequences(text_list, maxlen=self.sequence_len, value=0.)
    #     feed_dict = {self.averagePooling.input_x: input_x, self.averagePooling.input_length: input_length, self.averagePooling.dropout_keep_prob: 1}
    #     with self.sess.as_default():
    #         logits = self.sess.run(self.averagePooling.logits, feed_dict)
    #     return [l.index(max(l)) for l in logits]


# if __name__ == "__main__":
#     vocab, word2index = load_vocab()
#     vocab_size = len(vocab)
#     processed_dir = path.join(path.dirname(__file__), "../dataset")
#     stoplist_csv = path.join(processed_dir, "stoplist.csv")
#     with open(stoplist_csv, "r", encoding='UTF-8') as csv_file:
#         reader = csv.reader(csv_file)
#         reader.__next__()
#         stoplist = [row[0] for row in reader]
#     predictor = Predict(128, 100, vocab, word2index, stoplist)
#     while True:
#         text = input("text:\n")
#         if text == "quit":
#             break
#         prob = predictor.predict(text)
#         print("probability:")
#         print(prob)
#         print("\n")
