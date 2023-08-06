import sys
import argparse
import pickle

from dtsr.baselines import anova
from dtsr.config import Config
from dtsr.util import nested, filter_models

if __name__ == '__main__':

    argparser = argparse.ArgumentParser('''
            Performs pairwise likelihood ratio test for significance of differences in prediction quality between LME models fitted to data convolved using DTSR ("2-step" hypothesis test).
            Can be used for in-sample and out-of-sample evaluation.
            Can be used either to compare arbitrary sets of LME models or (using the "-a" flag) to perform hypothesis testing between DTSR models within one or more ablation sets. 
        ''')
    argparser.add_argument('config_path', help='Path to configuration (*.ini) file')
    argparser.add_argument('-m', '--models', nargs='*', default=[], help='List of model names for which to compute LRT tests. Regex permitted. If unspecified, uses all DTSR models.')
    argparser.add_argument('-a', '--ablation', action='store_true', help='Only compare models within an ablation set (those defined using the "ablate" param in the config file)')
    argparser.add_argument('-p', '--partition', type=str, default='dev', help='Name of partition to use (one of "train", "dev", "test")')
    args, unknown = argparser.parse_known_args()

    p = Config(args.config_path)

    models = filter_models(p.model_list, args.models, dtsr_only=True)

    sys.stderr.write('\n')

    if args.ablation:
        comparison_sets = {}
        for model_name in models:
            model_basename = model_name.split('!')[0]
            if model_basename not in comparison_sets:
                comparison_sets[model_basename] = []
            comparison_sets[model_basename].append(model_name)
        for model_name in p.model_list:
            model_basename = model_name.split('!')[0]
            if model_basename in comparison_sets and model_name not in comparison_sets[model_basename]:
                comparison_sets[model_basename].append(model_name)
    else:
        comparison_sets = {
            None: models
        }

    for s in comparison_sets:
        model_set = comparison_sets[s]
        if len(model_set) > 1:
            if s is not None:
                sys.stderr.write('Comparing models within ablation set "%s"...\n' %s)
            for i in range(len(model_set)):
                model_name_1 = model_set[i]
                lme_path_1 = p.outdir + '/' + model_name_1 + '/lmer_%s.obj' % args.partition
                with open(lme_path_1, 'rb') as m_file:
                    lme1 = pickle.load(m_file)

                for j in range(i+1, len(model_set)):
                    model_name_2 = model_set[j]
                    if nested(model_name_1, model_name_2) or not args.ablation:
                        lme_path_2 = p.outdir + '/' + model_name_2 + '/lmer_%s.obj' % args.partition
                        with open(lme_path_2, 'rb') as m_file:
                            lme2 = pickle.load(m_file)
                        anova_summary = str(anova(lme1.m, lme2.m))
                        name = '%s_v_%s' %(model_name_1, model_name_2)
                        out_path = p.outdir + '/' + name + '_2stepLRT_' + args.partition + '.txt'
                        with open(out_path, 'w') as f:
                            sys.stderr.write('Saving output to %s...\n' %out_path)
                            summary = '='*50 + '\n'
                            summary += 'Model comparison: %s vs %s\n' % (model_name_1, model_name_2)
                            summary += 'Partition: %s\n\n' %args.partition
                            if not lme1.converged():
                                summary += 'Model %s had the following convergence warnings:\n' %model_name_1
                                summary += '%s\n\n' %lme1.convergence_warnings()
                            if not lme2.converged():
                                summary += 'Model %s had the following convergence warnings:\n' %model_name_2
                                summary += '%s\n\n' %lme2.convergence_warnings()
                            summary += anova_summary + '\n'

                            f.write(summary)
                            sys.stdout.write(summary)
