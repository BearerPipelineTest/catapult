# Copyright 2020 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

from __future__ import absolute_import
from telemetry.internal.platform.tracing_agent import chrome_tracing_agent


# A class that uses ReportEvents mode for chrome tracing.
class ChromeReportEventsTracingAgent(chrome_tracing_agent.ChromeTracingAgent):
  @classmethod
  def IsSupported(cls, platform_backend):
    # TODO(crbug.com/1279968): Workaround to enable streaming for some fuchsia
    # platforms while progress is made on others.
    return (platform_backend.GetOSName() == 'fuchsia' and
            platform_backend.GetDeviceTypeName() in
            chrome_tracing_agent.NON_STREAM_FUCHSIA_BOARDS)

  def _GetTransferMode(self):
    return 'ReportEvents'

  def _StartStartupTracing(self, config):
    del config
    # Fuchsia doesn't support starting tracing with a config file
    return False

  def _RemoveTraceConfigFile(self):
    pass
