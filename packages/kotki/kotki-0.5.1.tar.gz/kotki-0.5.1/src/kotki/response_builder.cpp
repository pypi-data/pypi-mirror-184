#include "kotki/response_builder.h"
#include "kotki/response_options.h"

namespace marian {
namespace bergamot {

void ResponseBuilder::buildQualityScores(Histories &histories, Response &response) {
  qualityEstimator_.computeQualityScores(histories, response);
}

void ResponseBuilder::buildAlignments(Histories &histories, Response &response) {
  for (auto &history : histories) {
    // TODO(jerin): Change hardcode of nBest = 1
    NBestList onebest = history->nBest(1);

    Result result = onebest[0];  // Expecting only one result;
    Words words = std::get<0>(result);
    auto hyp = std::get<1>(result);
    auto softAlignment = hyp->tracebackAlignment();
    response.alignments.push_back(std::move(softAlignment));
  }
}

void ResponseBuilder::buildTranslatedText(Histories &histories, Response &response) {
  // Reserving length at least as much as source_ seems like a reasonable
  // thing to do to avoid reallocations.
  response.target.text.reserve(response.source.text.size());

  for (size_t sentenceIdx = 0; sentenceIdx < histories.size(); sentenceIdx++) {
    // TODO(jerin): Change hardcode of nBest = 1

    auto &history = histories[sentenceIdx];
    NBestList onebest = history->nBest(1);

    Result result = onebest[0];  // Expecting only one result;
    Words words = std::get<0>(result);

    std::string decoded;
    std::vector<string_view> targetSentenceMappings;
    vocabs_.target()->decodeWithByteRanges(words, decoded, targetSentenceMappings, /*ignoreEOS=*/false);

    // For each sentence, prepend the filler text between the corresponding
    // source-sentence and the source-sentence before.
    string_view pre = response.source.gap(sentenceIdx);
    response.target.appendSentence(pre, targetSentenceMappings.begin(), targetSentenceMappings.end());

    // If this is the last history to be decoded and translated-text
    // constructed, append the text till the end, which could be spaces or
    // empty.
    if (sentenceIdx + 1 == histories.size()) {
      response.target.appendEndingWhitespace(response.source.gap(sentenceIdx + 1));
    }
  }
}

}  // namespace bergamot
}  // namespace marian
