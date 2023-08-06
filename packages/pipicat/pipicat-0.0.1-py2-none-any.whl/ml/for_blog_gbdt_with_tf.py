
'''
For the blog: Build GBDT model with tensorflow
Yi Ding, 1/18/18
Most code from github: tensorflow

'''

from tensorflow.contrib.boosted_trees.estimator_batch import custom_export_strategy
from tensorflow.contrib.boosted_trees.estimator_batch.estimator import GradientBoostedDecisionTreeRegressor
from tensorflow.contrib.boosted_trees.proto import learner_pb2
from tensorflow.contrib.layers.python.layers import feature_column
from tensorflow.contrib.learn import learn_runner



# Main config - creates a TF Boosted Trees Estimator based on flags.
def _get_tfbt(output_dir, feature_cols):
  """Configures TF Boosted Trees estimator based on flags."""
  learner_config = learner_pb2.LearnerConfig()
  learner_config.learning_rate_tuner.fixed.learning_rate = FLAGS.learning_rate
  learner_config.regularization.l1 = 0.0
  learner_config.regularization.l2 = FLAGS.l2
  learner_config.constraints.max_tree_depth = FLAGS.depth

  run_config = tf.contrib.learn.RunConfig(save_checkpoints_secs=300)

  # Create a TF Boosted trees regression estimator.
  estimator = GradientBoostedDecisionTreeRegressor(
      learner_config=learner_config,
      # This should be the number of examples. For large datasets it can be
      # larger than the batch_size.
      examples_per_layer=FLAGS.batch_size,
      feature_columns=feature_cols,
      label_dimension=1,
      model_dir=output_dir,
      num_trees=FLAGS.num_trees,
      center_bias=False,
      config=run_config)
  return estimator