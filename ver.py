import gpt_2_simple as gpt2
content_feed = 'love_letter'
sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess, run_name=content_feed)

single_text = gpt2.generate(sess,
              run_name=content_feed,
              length=250,
              temperature=0.8,
              prefix="Today, I ",
              model_name='355M',
              nsamples=1,
              batch_size=1,
              return_as_list=True
              )[0]
single_text = str(single_text)
print(single_text)
