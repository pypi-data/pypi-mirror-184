def _print_impact_list(filtered_input):
    out = ''
    for i, x in enumerate(filtered_input):
        out += f"   {x['token']:15}   {x['num_occurrences']:^10}     {x['mean_feature_impact']:^12.4f}      " \
               f"{x['mean_abs_feature_impact']:^14.4f}\n"

    return out


class NLPGlobalFeatureImpactResult:
    def __init__(self, result_named_tuple, n_inputs, min_support):
        self.raw_output = result_named_tuple
        self.min_support = min_support
        self.n_inputs = n_inputs

        self.impact_by_output = {}

        if isinstance(result_named_tuple.output_name, str):  # compatibility with compute_all_classes == False
            self.output_names = [result_named_tuple.output_name]

            # Unpack raw output to make it easier to use
            for output_index, output_name in enumerate(self.output_names):
                self.impact_by_output[output_name] = [{'token': word,
                                                       'num_occurrences': dat['num_occurrences'],
                                                       'mean_abs_feature_impact': dat['mean_abs_feature_impact'],
                                                       'mean_feature_impact': dat['mean_feature_impact']}
                                                      for word, dat in self.raw_output.impact_table.items()]
        else:  # compute_all_classes == True
            self.output_names = result_named_tuple.output_name

            # Unpack raw output to make it easier to use
            for output_index, output_name in enumerate(self.output_names):
                self.impact_by_output[output_name] = [{'token': word,
                                                       'num_occurrences': dat['num_occurrences'],
                                                       'mean_abs_feature_impact': dat['mean_abs_feature_impact'][
                                                           output_index],
                                                       'mean_feature_impact': dat['mean_feature_impact'][output_index]}
                                                      for word, dat in self.raw_output.impact_table.items()]

    def __repr__(self):
        return self._pretty_nlp_impact()

    def pretty_print_nlp_impact(self, top_n=8, min_occurrences=0):
        """
        Print the nlp feature impact result with nice formatting

        top_n (int [8]) -- How many of the largest positive and negative attributions to display.
        min_occurrences (int [0]) -- Minimum number of occurrences of a token required to include in output.
        """
        print(self._pretty_nlp_impact(top_n, min_occurrences))

    def _pretty_nlp_impact(self, top_n=8, min_occurrences=0):
        raw_impact = self.raw_output

        out = f"Calculation performed using {self.n_inputs} text samples.\n" \
              f"Results were returned for tokens with at least {self.min_support} occurrence(s).\n"

        n_tokens = len(raw_impact.impact_table)
        n_supported_tokens = len([_ for _, v in raw_impact.impact_table.items() if v['num_occurrences']
                                  >= min_occurrences])

        out += f'{n_tokens} distinct tokens returned.\n'
        if min_occurrences != 0:
            out += f'{n_supported_tokens} tokens meet the requested display threshold of {min_occurrences}' \
                   f'occurrences.\n\n'

        out += '\n'

        for output_name in self.output_names:

            filtered_nonneg = [x for x in self.impact_by_output[output_name] if
                               x['num_occurrences'] >= min_occurrences and x['mean_feature_impact'] >= 0]

            filtered_neg = [x for x in self.impact_by_output[output_name] if
                            x['num_occurrences'] >= min_occurrences and x['mean_feature_impact'] < 0]

            filtered_nonneg = sorted(filtered_nonneg, key=lambda x: x['mean_feature_impact'], reverse=True)[
                                    :top_n]
            filtered_neg = list(reversed(sorted(filtered_neg, key=lambda x: x['mean_feature_impact'])))[-top_n:]

            out += f'--- output: {output_name} ---\n\n'

            out += f"   {'token':15s}   {'occurrences':10s}  {'<feature impact>':12s}  {'<|feature impact|>':12s}\n"
            out += f"   {'-----':15s}   {'-----------':10s}  {'----------------':12s}  {'------------------':12s}\n"

            if len(filtered_nonneg):
                out += _print_impact_list(filtered_nonneg)
            else:
                out += '   There are no negative contributons with more than {min_occurrances} occurrances.\n'

            if n_tokens > 2 * top_n:
                out += f'\n  <skipping {n_tokens - len(filtered_nonneg) - len(filtered_neg)} ' \
                       f'lower-absolute-impact tokens>\n\n'

            if len(filtered_neg):
                out += _print_impact_list(filtered_neg)
            else:
                out += '   There are no negative contributons with more than {min_occurrances} occurrances.\n'

            out += '\n\n'

        return out
