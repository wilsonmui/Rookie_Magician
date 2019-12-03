import gpt_2_simple as gpt2
import tensorflow as tf

def load(book):
    tf.reset_default_graph()
    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess, run_name=book)
    return sess
def generate(book, length, temperature, prefix, sess):
    print("generating...")
    single_text = gpt2.generate(sess,
                  run_name=book,
                  length=length,
                  temperature=temperature,
                  prefix=prefix,
                  model_name='355M',
                  nsamples=1,
                  batch_size=1,
                  return_as_list=True
                  )[0]
    single_text = str(single_text)
    print("generated.")
    return single_text

def main():
    book = "love_letter"
    length = 150
    temperature = 0.7
    prefix = "So, do you"
    sess = load(book)
    text_result = generate(book, length, temperature ,prefix, sess)
    print(text_result)
if __name__ == '__main__':
    main()
