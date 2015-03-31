from pyasn1.type import univ, namedtype, namedval, constraint, tag, char

class ChargingUnitsAddition(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(2, 2)


class ResponseTimeCategory(univ.Enumerated):
  namedValues = namedval.NamedValues(
    ('lowdelay', 0),
    ('delaytolerant', 1),
  )


class SSRequest(univ.Enumerated):
  namedValues = namedval.NamedValues(
    ('registration', 0),
    ('erasure', 1),
    ('activation', 2),
    ('deactivation', 3),
    ('interrogation', 4),
    ('invoke', 5),
    ('registerPassword', 6),
    ('processUSSD', 7),
  )


class DeliveryOfErroneousSDU(univ.Enumerated):
  namedValues = namedval.NamedValues(
    ('yes', 0),
    ('no', 1),
    ('noErrorDetectionConsideration', 2),
  )


class DecipheringKeys(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(8, 15)


class LCSAccuracy(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(1, 1)


class GenericNumber(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(3, 17)


class BitRate(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(1, 1)


class TransitCarrierInfo(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(7, 96)


class FrequencyBandSupported(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(1, 1)


class TAC(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(3, 4)


class ServiceSwitchingType(univ.Enumerated):
  namedValues = namedval.NamedValues(
    ('speechToFax', 0),
    ('faxToSpeech', 1),
  )


class UserToUserService1Information(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(2, 2)


class CallPosition(univ.Enumerated):
  namedValues = namedval.NamedValues(
    ('valueUsedForAllCallsToDetermineIfOutputToTakePlace', 0),
    ('callHasReachedCongestionOrBusyState', 1),
    ('callHasOnlyReachedThroughConnection', 2),
    ('b-AnswerHasBeenReceived', 3),
  )


class UILayer1Protocol(univ.Enumerated):
  namedValues = namedval.NamedValues(
    ('v110_X30', 1),
    ('g711mulaw', 2),
    ('g711Alaw', 3),
    ('g721_32000bps_I460', 4),
    ('h221_H242', 5),
    ('h223_H245', 6),
    ('nonITU_T', 7),
    ('v120', 8),
    ('x31', 9),
    ('vSELP_Speech', 10),
  )


class TrafficClass(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(1, 1)


class ServiceFeatureCode(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(2, 2)


class ChannelCodings(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(1, 1)


class FaultCode(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(2, 2)


class DisconnectingParty(univ.Enumerated):
  namedValues = namedval.NamedValues(
    ('callingPartyRelease', 0),
    ('calledPartyRelease', 1),
    ('networkRelease', 2),
  )


class RTCSessionID(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(16, 16)


class AoCCurrencyAmountSent(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(4, 4)


class OperationIdentifier(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(1, 1)


class TeleServiceCode(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(1, 1)


class TariffSwitchInd(univ.Enumerated):
  namedValues = namedval.NamedValues(
    ('noTariffSwitch', 0),
    ('tariffSwitchAfterStartOfCharging', 2),
  )


class RTCNotInvokedReason(univ.Enumerated):
  namedValues = namedval.NamedValues(
    ('emergencyCall', 0),
    ('callToSpecialDestination', 1),
    ('callLegNotToBeCharged', 2),
    ('smsNotToBeCharged', 3),
    ('mcaSMSFreeOfCharge', 4),
    ('undeterminedRoamingPLMN', 5),
  )


class TBCDString(univ.OctetString):
  pass


class ChargeInformation(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(2, 33)


class NumberOfChannels(univ.Enumerated):
  namedValues = namedval.NamedValues(
    ('oneTrafficChannel', 0),
    ('twoTrafficChannels', 1),
    ('threeTrafficChannels', 2),
    ('fourTrafficChannels', 3),
    ('fiveTrafficChannels', 4),
    ('sixTrafficChannels', 5),
    ('sevenTrafficChannels', 6),
    ('eightTrafficChannels', 7),
  )


class SpeechCoderPreferenceList(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(1, 6)


class EosInfo(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(1, 1)


class INMarkingOfMS(univ.Enumerated):
  namedValues = namedval.NamedValues(
    ('originatingINService', 1),
    ('terminatingINService', 2),
    ('originatingINCategoryKeyService', 3),
    ('terminatingINCategoryKeyService', 4),
    ('originatingCAMELService', 5),
    ('terminatingCAMELService', 6),
    ('originatingExtendedCAMELServiceWithINCapabilityIndicator', 7),
    ('terminatingExtendedCAMELServiceWithINCapabilityIndicator', 8),
    ('originatingExtendedCAMELServiceWithOriginatingINCategoryKey', 9),
    ('terminatingExtendedCAMELServiceWithTerminatingINCategoryKey', 10),
    ('subscriberDialledCAMELService', 11),
    ('subscriberDialledCAMELServiceAndOriginatingCAMELService', 12),
    ('visitedTerminatingCAMELService', 13),
  )


class RoamingPriorityLevel(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(1, 1)


class EMLPPPriorityLevel(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(1, 1)


class ChargingOrigin(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(1, 1)


class TypeOfCalledSubscriber(univ.Enumerated):
  namedValues = namedval.NamedValues(
    ('pSTNSubscriber', 0),
    ('iSDNSubscriber', 1),
    ('unknownSubscriber', 2),
  )


class TransferDelay(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(2, 2)


class TransparencyIndicator(univ.Enumerated):
  namedValues = namedval.NamedValues(
    ('transparent', 0),
    ('nonTransparent', 1),
  )


class DefaultSMS_Handling(univ.Enumerated):
  namedValues = namedval.NamedValues(
    ('continueTransaction', 0),
    ('releaseTransaction', 1),
  )


class CallIDNumber(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(3, 3)


class RecordSequenceNumber(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(3, 3)


class GlobalCallReference(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(3, 15)


class AddressStringExtended(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(1, 20)


class CarrierInfo(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(2, 3)


class MessageReference(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(1, 1)


class Route(char.IA5String):
  subtypeSpec = char.IA5String.subtypeSpec + constraint.ValueSizeConstraint(1, 7)


class FirstRadioChannelUsed(univ.Enumerated):
  namedValues = namedval.NamedValues(
    ('fullRateChannel', 0),
    ('halfRateChannel', 1),
  )


class TariffClass(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(2, 2)


class ServiceKey(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(4, 4)


class IntermediateRate(univ.Enumerated):
  namedValues = namedval.NamedValues(
    ('rate8KbitPerSecondUsed', 2),
    ('rate16KbitPerSecondUsed', 3),
  )


class Counter(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(1, 4)


class UserToUserInformation(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(1, 33)


class C7ChargingMessage(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(8, 8)


class RegionalServiceUsed(univ.Enumerated):
  namedValues = namedval.NamedValues(
    ('localSubscription', 0),
    ('regionalSubcription', 1),
    ('subscriptionWithTariffAreas', 2),
    ('regionalSubcriptionAndSubscriptionWithTariffAreas', 3),
  )


class UserRate(univ.Enumerated):
  namedValues = namedval.NamedValues(
    ('uRIndNeg', 0),
    ('uR600bps', 1),
    ('uR1200bps', 2),
    ('uR2400bps', 3),
    ('uR3600bps', 4),
    ('uR4800bps', 5),
    ('uR7200bps', 6),
    ('uR8000bps', 7),
    ('uR9600bps', 8),
    ('uR14400bps', 9),
    ('uR16000bps', 10),
    ('uR19200bps', 11),
    ('uR32000bps', 12),
    ('uR38400bps', 13),
    ('uR48000bps', 14),
    ('uR56000bps', 15),
    ('uR64000bps', 16),
    ('uR38400bps1', 17),
    ('uR57600bps', 18),
    ('uR28800bps', 19),
    ('uR134-5bps', 21),
    ('uR100bps', 22),
    ('uR75bps_1200bps', 23),
    ('uR1200bps_75bps', 24),
    ('uR50bps', 25),
    ('uR75bps', 26),
    ('uR110bps', 27),
    ('uR150bps', 28),
    ('uR200bps', 29),
    ('uR300bps', 30),
    ('uR12000bps', 31),
  )


class SMSResult(univ.Enumerated):
  namedValues = namedval.NamedValues(
    ('unsuccessfulMOSMSDeliverytoSMSCDuetoCAMELReason', 0),
    ('unsuccessfulMOSMSDeliverytoSMSCDuetoOtherReason', 1),
    ('unsuccessfulMTSMSDeliverytoMSDuetoCAMELReason', 2),
    ('unsuccessfulMTSMSDeliverytoMSDuetoOtherReason', 3),
    ('unsuccellfulMOSMSDeliverytoSMSCDuetoRTCFAReason', 4),
    ('unsuccessfulMTSMSDeliverytoMSDuetoRTCFAReason', 5),
  )


class LCSClientType(univ.Enumerated):
  namedValues = namedval.NamedValues(
    ('emergencyServices', 0),
    ('valueAddedServices', 1),
    ('plmnOperatorServices', 2),
    ('lawfulInterceptServices', 3),
  )


class SpeechCoderVersion(univ.Enumerated):
  namedValues = namedval.NamedValues(
    ('fullRateVersion1', 0),
    ('fullRateVersion2', 1),
    ('fullRateVersion3', 2),
    ('halfRateVersion1', 3),
    ('halfRateVersion2', 4),
    ('halfRateVersion3', 5),
  )


class OutputForSubscriber(univ.Enumerated):
  namedValues = namedval.NamedValues(
    ('callingParty', 0),
    ('calledParty', 1),
    ('callingAndCalledParty', 2),
  )


class MessageTypeIndicator(univ.Enumerated):
  namedValues = namedval.NamedValues(
    ('sMSdeliverSCtoMS', 0),
    ('sMSdeliveReportMStoSC', 1),
    ('sMSstatusReportSCtoMS', 2),
    ('sMScommanMStoSC', 3),
    ('sMSsubmitMStoSC', 4),
    ('sMSsubmitReportSCtoMS', 5),
    ('reservedMTIValue', 6),
  )


class UnsuccessfulPositioningDataReason(univ.Enumerated):
  namedValues = namedval.NamedValues(
    ('systemError', 0),
    ('userDeniedDueToPrivacyVerification', 1),
  )


class CRIIndicator(univ.Enumerated):
  namedValues = namedval.NamedValues(
    ('chargeRateInformationAcknowledged', 1),
    ('chargeRateInformationNotAcknowledged', 2),
  )


class TriggerDetectionPoint(univ.Enumerated):
  namedValues = namedval.NamedValues(
    ('originatingCallAttemptAuthorized', 1),
    ('collectedInformation', 2),
    ('analyzedInformation', 3),
    ('originatingCallAttemptRouteSelectFailure', 4),
    ('originatingCallAttemptCalledPartyBusy', 5),
    ('originatingCallAttemptCalledPartyNotAnswer', 6),
    ('originatingCallAttemptCalledPartyAnswer', 7),
    ('originatingCallAttemptMid-CallEventDetected', 8),
    ('originatingCallAttemptCallDisconnecting', 9),
    ('originatingCallAttemptCallAbandon', 10),
    ('terminatingCallAttemptAuthorized', 12),
    ('terminatingCallAttemptCalledPartyBusy', 13),
    ('terminatingCallAttemptNoAnswer', 14),
    ('terminatingCallAttemptAnswer', 15),
    ('terminatingCallAttemptMid-CallEventDetected', 16),
    ('terminatingCallAttemptCallDisconnect', 17),
    ('terminatingCallAttemptCallAbandon', 18),
    ('terminatingCallAttemptCallReAnswer', 247),
    ('terminatingCallAttemptCallSuspended', 248),
    ('terminatingCallAttemptCalledPartyNotReachable', 249),
    ('terminatingCallAttemptAlerting', 250),
    ('terminatingCallAttemptRouteSelectFailure', 251),
    ('originatingCallAttemptCalledPartyReAnswer', 252),
    ('originatingCallAttemptCallSuspended', 253),
    ('originatingCallAttemptCalledPartyNotReachable', 254),
    ('originatingCallAttemptAlerting', 255),
  )


class TypeOfSignalling(univ.Enumerated):
  namedValues = namedval.NamedValues(
    ('iSUPIsNotAppliedAllTheWay', 0),
    ('iSUPIsAppliedAllTheWay', 1),
    ('unknownSignalling', 2),
  )


class AirInterfaceUserRate(univ.Enumerated):
  namedValues = namedval.NamedValues(
    ('aIUR9600bps', 1),
    ('aIUR14400bps', 2),
    ('aIUR19200bps', 3),
    ('aIUR28800bps', 5),
    ('aIUR38400bps', 6),
    ('aIUR43200bps', 7),
    ('aIUR57600bps', 8),
    ('aIUR38400bps1', 9),
    ('aIUR38400bps2', 10),
    ('aIUR38400bps3', 11),
    ('aIUR38400bps4', 12),
  )


class PresentationAndScreeningIndicator(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(1, 1)


class DefaultCallHandling(univ.Enumerated):
  namedValues = namedval.NamedValues(
    ('continueCall', 0),
    ('releaseCall', 1),
  )


class Distributed(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(4, 4)


class ChargingCase(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(2, 2)


class CallAttemptState(univ.Enumerated):
  namedValues = namedval.NamedValues(
    ('initialState', 0),
    ('callSentState', 1),
    ('callRejectedState', 2),
    ('callOfferedState', 3),
    ('noResponseState', 4),
    ('alertingState', 5),
    ('unknownCallState', 6),
    ('callActiveState', 7),
  )


class OutputType(univ.Enumerated):
  namedValues = namedval.NamedValues(
    ('noOutput', 0),
    ('iCIoutputForCallingSubscriber', 1),
    ('iCIOutputForCalledSubscriber', 2),
    ('iCIOutputForCallingAndCalledSubscribers', 3),
    ('tTOutputOnly', 4),
    ('tTAndICIForCallingSubscriber', 5),
    ('tTAndICIForCalledSubscriber', 6),
    ('tTAndICIForCallingAndCalledSubscribers', 7),
  )


class SubscriberState(univ.Enumerated):
  namedValues = namedval.NamedValues(
    ('detached', 0),
    ('attached', 1),
    ('implicitDetached', 2),
  )


class SelectedCodec(univ.Enumerated):
  namedValues = namedval.NamedValues(
    ('gSMFullRate', 0),
    ('gSMHalfRate', 1),
    ('gSMEnhancedFullRate', 2),
    ('fullRateAdaptiveMultiRate', 3),
    ('halfRateAdaptiveMultiRate', 4),
    ('uMTSAdaptiveMultiRate', 5),
    ('uMTSAdaptiveMultiRate2', 6),
    ('tDMAEnhancedFullRate', 7),
    ('pDCEnhancedFullRate', 8),
    ('inmarsatCoding', 15),
  )


class AgeOfLocationEstimate(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(2, 2)


class ChargeAreaCode(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(3, 3)


class CUGIndex(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(2, 2)


class UserTerminalPosition(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(7, 7)


class LCSDeferredEventType(univ.Enumerated):
  namedValues = namedval.NamedValues(
    ('deferred_MT_UEreachableEvent', 0),
  )


class SSCode(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(1, 1)


class TypeOfCallingSubscriber(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(1, 1)


class OptimalRoutingType(univ.Enumerated):
  namedValues = namedval.NamedValues(
    ('optimalRoutingAtLateCallForwarding', 0),
  )


class PositionAccuracy(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(2, 2)


class Date(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(3, 4)


class UserClass(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(1, 1)


class NumberOfShortMessage(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(2, 2)


class BearerServiceCode(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(1, 1)


class FixedNetworkUserRate(univ.Enumerated):
  namedValues = namedval.NamedValues(
    ('fNUR9600bps', 1),
    ('fNUR14400bps', 2),
    ('fNUR19200bps', 3),
    ('fNUR28800bps', 4),
    ('fNUR38400bps', 5),
    ('fNUR48000bps', 6),
    ('fNUR56000bps', 7),
    ('fNUR64000bps', 8),
    ('fNURautobauding', 9),
  )


class GenericDigits(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(2, 15)


class RadioChannelProperty(univ.Enumerated):
  namedValues = namedval.NamedValues(
    ('halfRateChannel', 0),
    ('fullRateChannel', 1),
    ('dualRateHalfRatePreferred', 2),
    ('dualRateFullRatePreferred', 3),
    ('twoFullRateChannels', 4),
    ('threeFullRateChannels', 5),
    ('fourFullRateChannels', 6),
    ('twoAssignedAirTimeSlots', 7),
    ('fourAssignedAirTimeSlots', 8),
    ('sixAssignedAirTimeSlots', 9),
    ('eightAssignedAirTimeSlots', 10),
    ('twelveAssignedAirTimeSlots', 11),
    ('sixteenAssignedAirtimeSlots', 12),
    ('twoDownlinkOneUplinkAssignedAirTimeSlots', 13),
    ('fourDownlinkOneUplinkAssignedAirTimeSlots', 14),
  )


class Time(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(3, 4)


class RANAPCauseCode(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(1, 1)


class SwitchIdentity(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(2, 2)


class BSSMAPCauseCode(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(1, 2)


class NetworkCallReference(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(5, 5)


class SSFChargingCase(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(2, 2)


class CarrierSelectionSubstitutionInformation(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(1, 1)


class ApplicationIdentifier(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(2, 2)


class RTCDefaultServiceHandling(univ.Enumerated):
  namedValues = namedval.NamedValues(
    ('serviceAllowed', 0),
    ('serviceNotAllowed', 1),
  )


class LegID(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(1, 1)


class MiscellaneousInformation(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(1, 1)


class TargetRNCid(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(7, 7)


class InternalCauseAndLoc(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(2, 2)


class OriginatedCode(univ.Enumerated):
  namedValues = namedval.NamedValues(
    ('callOriginatingFromOwnSubscriberInSSN', 0),
    ('callOriginatingFromOwnSubscriberInGSN', 1),
    ('callOriginatingFromIncomingTrunk', 2),
    ('callOriginatingFromSUSblock', 3),
    ('callOriginatingFromOMSblock', 4),
    ('testCallTowardsIL-OL-BL', 5),
    ('testCallWithIndividualSelectionOfB-Subscriber', 6),
    ('testCallWithIndividualSelectionExceptB-Subscriber', 7),
    ('testCallWithSelectionInSpecifiedRoute', 8),
    ('operator', 9),
  )


class SubscriptionType(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(1, 1)


class ExchangeIdentity(char.IA5String):
  subtypeSpec = char.IA5String.subtypeSpec + constraint.ValueSizeConstraint(1, 15)


class GlobalTitleAndSubSystemNumber(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(5, 13)


class TrafficActivityCode(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(5, 5)


class CUGInterlockCode(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(4, 4)


class RTCFailureIndicator(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(2, 2)


class ChargingIndicator(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(1, 1)


class INServiceTrigger(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(2, 2)


class CarrierInformation(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(1, 1)


class CauseCode(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(1, 1)


class EndToEndAccessDataMap(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(1, 1)


class MobileUserClass2(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(1, 1)


class MobileUserClass1(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(1, 1)


class ChargedParty(univ.Enumerated):
  namedValues = namedval.NamedValues(
    ('chargingOfCallingSubscriber', 0),
    ('chargingOfCalledSubscriber', 1),
    ('noCharging', 2),
  )


class ChangeInitiatingParty(univ.Enumerated):
  namedValues = namedval.NamedValues(
    ('userInitiated', 0),
    ('networkInitiated', 1),
  )


class AsyncSyncIndicator(univ.Enumerated):
  namedValues = namedval.NamedValues(
    ('syncData', 0),
    ('asyncData', 1),
  )


class TypeOfLocationRequest(univ.Enumerated):
  namedValues = namedval.NamedValues(
    ('mT_LocationRequestCurrentLocation', 0),
    ('mT_LocationRequestCurrentOrLastKnownLocation', 1),
    ('mO_LocationRequestLocEstimateToMS', 2),
    ('mO_LocationRequestLocEstimateToThirdParty', 3),
    ('mO_LocationRequestAssistData', 4),
    ('mO_LocationRequestDeciphKeys', 5),
    ('nI_LocationRequest', 6),
    ('mT_LocationRequestDeferred', 7),
  )


class FreeFormatData(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(1, 160)


class LocationInformation(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(7, 7)


class GlobalTitle(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(4, 12)


class OriginatingLineInformation(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(1, 1)


class PartialOutputRecNum(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(1, 1)


class ErrorRatio(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(2, 2)


class NumberOfOperations(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(1, 1)


class ChannelAllocationPriorityLevel(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(1, 1)


class LocationEstimate(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(1, 91)


class PositioningDelivery(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(1, 1)


class C7CHTMessage(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(5, 5)


class GSMCallReferenceNumber(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(1, 8)


class PointCodeAndSubSystemNumber(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(4, 4)


class Single(univ.Enumerated):
  namedValues = namedval.NamedValues(
    ('aPartyToBeCharged', 0),
    ('bPartyToBeCharged', 1),
    ('cPartyToBeCharged', 2),
    ('otherPartyToBeCharged', 3),
  )


class LocationCode(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(1, 1)


class NumberOfMeterPulses(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(3, 3)


class RedirectionCounter(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(1, 1)


class LevelOfCAMELService(univ.BitString):
  namedValues = namedval.NamedValues(
    ('basic', 0),
    ('callDurationSupervision', 1),
    ('onlineCharging', 2),
  )


class AddressString(univ.OctetString):
  subtypeSpec = univ.OctetString.subtypeSpec + constraint.ValueSizeConstraint(1, 20)


class ServiceCode(TBCDString):
  subtypeSpec = TBCDString.subtypeSpec + constraint.ValueSizeConstraint(1, 2)


class CAMELTDPData(univ.Sequence):
  componentType = namedtype.NamedTypes(
    namedtype.NamedType('serviceKey', ServiceKey().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0))),
    namedtype.NamedType('gsmSCFAddress', AddressString().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 9), implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1))),
  )


class AccountCode(TBCDString):
  subtypeSpec = TBCDString.subtypeSpec + constraint.ValueSizeConstraint(1, 5)


class TriggerData(univ.Sequence):
  componentType = namedtype.NamedTypes(
    namedtype.NamedType('triggerDetectionPoint', TriggerDetectionPoint().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0))),
    namedtype.NamedType('serviceKey', ServiceKey().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1))),
    namedtype.NamedType('sCPAddress', univ.Choice(
      componentType = namedtype.NamedTypes(
        namedtype.NamedType('co_located', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2))),
        namedtype.NamedType('pointCodeAndSubSystemNumber', PointCodeAndSubSystemNumber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3))),
        namedtype.NamedType('globalTitle', GlobalTitle().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4))),
        namedtype.NamedType('globalTitleAndSubSystemNumber', GlobalTitleAndSubSystemNumber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 5))),
      )
    )),
  )


class CarrierIdentificationCode(TBCDString):
  subtypeSpec = TBCDString.subtypeSpec + constraint.ValueSizeConstraint(1, 3)


class IMEISV(TBCDString):
  subtypeSpec = TBCDString.subtypeSpec + constraint.ValueSizeConstraint(8, 8)


class CRIToMS(TBCDString):
  subtypeSpec = TBCDString.subtypeSpec + constraint.ValueSizeConstraint(14, 14)


class TransitINOutgoingCall(univ.Set):
  componentType = namedtype.NamedTypes(
    namedtype.OptionalNamedType('tAC', TAC().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0))),
    namedtype.OptionalNamedType('callIdentificationNumber', CallIDNumber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1))),
    namedtype.OptionalNamedType('recordSequenceNumber', RecordSequenceNumber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2))),
    namedtype.OptionalNamedType('outgoingRoute', Route().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3))),
    namedtype.OptionalNamedType('subscriptionType', SubscriptionType().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4))),
    namedtype.OptionalNamedType('incompleteCallDataIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 5))),
    namedtype.OptionalNamedType('incompleteCompositeCDRIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 6))),
    namedtype.OptionalNamedType('lastPartialOutput', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 7))),
    namedtype.OptionalNamedType('partialOutputRecNum', PartialOutputRecNum().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 8))),
    namedtype.OptionalNamedType('restartDuringOutputIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 9))),
    namedtype.OptionalNamedType('exchangeIdentity', ExchangeIdentity().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 10))),
    namedtype.OptionalNamedType('restartDuringCall', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 11))),
    namedtype.OptionalNamedType('networkCallReference', NetworkCallReference().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 12))),
    namedtype.OptionalNamedType('iCIOrdered', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 13))),
    namedtype.OptionalNamedType('outputForSubscriber', OutputForSubscriber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 14))),
    namedtype.OptionalNamedType('switchIdentity', SwitchIdentity().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 15))),
    namedtype.OptionalNamedType('disconnectionDueToSystemRecovery', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 16))),
    namedtype.OptionalNamedType('forloppDuringOutputIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 17))),
    namedtype.OptionalNamedType('tariffClass', TariffClass().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 18))),
    namedtype.OptionalNamedType('forloppReleaseDuringCall', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 19))),
    namedtype.OptionalNamedType('c7ChargingMessage', C7ChargingMessage().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 20))),
    namedtype.OptionalNamedType('c7FirstCHTMessage', C7CHTMessage().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 21))),
    namedtype.OptionalNamedType('c7SecondCHTMessage', C7CHTMessage().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 22))),
    namedtype.OptionalNamedType('contractorNumber', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 23))),
    namedtype.OptionalNamedType('calledPartyMNPInfo', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 24))),
    namedtype.OptionalNamedType('globalCallReference', GlobalCallReference().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 25))),
    namedtype.OptionalNamedType('outputType', OutputType().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 102))),
  )


class IMSI(TBCDString):
  subtypeSpec = TBCDString.subtypeSpec + constraint.ValueSizeConstraint(3, 8)


class HandOverEventModule(univ.Set):
  componentType = namedtype.NamedTypes(
    namedtype.OptionalNamedType('tAC', TAC().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0))),
    namedtype.OptionalNamedType('timeForEvent', Time().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1))),
    namedtype.OptionalNamedType('rNCidOfTargetRNC', TargetRNCid().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2))),
    namedtype.OptionalNamedType('incompleteCallDataIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3))),
    namedtype.OptionalNamedType('targetLocationInformation', LocationInformation().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4))),
    namedtype.OptionalNamedType('radioChannelProperty', RadioChannelProperty().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 5))),
    namedtype.OptionalNamedType('channelCodingUsed', ChannelCodings().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 6))),
    namedtype.OptionalNamedType('bSSMAPCauseCode', BSSMAPCauseCode().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 7))),
    namedtype.OptionalNamedType('rANAPCauseCode', RANAPCauseCode().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 8))),
  )


class GenericNumbersSet(univ.SetOf):
  componentType = GenericNumber()
subtypeSpec = univ.SetOf.subtypeSpec + constraint.ValueSizeConstraint(1, 20)


class MultimediaInformation(univ.Sequence):
  componentType = namedtype.NamedTypes(
    namedtype.OptionalNamedType('userRate', UserRate().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0))),
    namedtype.OptionalNamedType('asyncSyncIndicator', AsyncSyncIndicator().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1))),
    namedtype.NamedType('uILayer1Protocol', UILayer1Protocol().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2))),
  )


class MSOriginatingSMSinSMS_IWMSC(univ.Set):
  componentType = namedtype.NamedTypes(
    namedtype.OptionalNamedType('tAC', TAC().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0))),
    namedtype.OptionalNamedType('callIdentificationNumber', CallIDNumber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1))),
    namedtype.OptionalNamedType('recordSequenceNumber', RecordSequenceNumber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2))),
    namedtype.OptionalNamedType('callingPartyNumber', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3))),
    namedtype.OptionalNamedType('dateForStartOfCharge', Date().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4))),
    namedtype.OptionalNamedType('timeForStartOfCharge', Time().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 5))),
    namedtype.OptionalNamedType('chargedParty', ChargedParty().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 6))),
    namedtype.OptionalNamedType('exchangeIdentity', ExchangeIdentity().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 7))),
    namedtype.OptionalNamedType('mSCIdentification', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 8))),
    namedtype.OptionalNamedType('teleServiceCode', TeleServiceCode().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 9))),
    namedtype.OptionalNamedType('serviceCentreAddress', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 10))),
    namedtype.OptionalNamedType('miscellaneousInformation', MiscellaneousInformation().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 11))),
    namedtype.OptionalNamedType('incompleteCallDataIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 12))),
    namedtype.OptionalNamedType('restartDuringOutputIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 13))),
    namedtype.OptionalNamedType('forloppDuringOutputIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 14))),
    namedtype.OptionalNamedType('switchIdentity', SwitchIdentity().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 15))),
    namedtype.OptionalNamedType('outputType', OutputType().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 102))),
  )


class EventCRIToMS(TBCDString):
  subtypeSpec = TBCDString.subtypeSpec + constraint.ValueSizeConstraint(4, 4)


class ISDNSSInvocationEventModule(univ.Set):
  componentType = namedtype.NamedTypes(
    namedtype.OptionalNamedType('trafficActivityCode', TrafficActivityCode().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0))),
    namedtype.OptionalNamedType('incompleteCallDataIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1))),
  )


class GenericDigitsSet(univ.SetOf):
  componentType = GenericDigits()
subtypeSpec = univ.SetOf.subtypeSpec + constraint.ValueSizeConstraint(1, 20)


class ISDNOriginating(univ.Set):
  componentType = namedtype.NamedTypes(
    namedtype.OptionalNamedType('trafficActivityCode', TrafficActivityCode().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0))),
    namedtype.OptionalNamedType('callIdentificationNumber', CallIDNumber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1))),
    namedtype.OptionalNamedType('recordSequenceNumber', RecordSequenceNumber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2))),
    namedtype.OptionalNamedType('typeOfCallingSubscriber', TypeOfCallingSubscriber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3))),
    namedtype.OptionalNamedType('chargedCallingPartyNumber', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4))),
    namedtype.OptionalNamedType('calledPartyNumber', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 5))),
    namedtype.OptionalNamedType('disconnectingParty', DisconnectingParty().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 6))),
    namedtype.OptionalNamedType('dateForStartOfCharge', Date().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 7))),
    namedtype.OptionalNamedType('timeForStartOfCharge', Time().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 8))),
    namedtype.OptionalNamedType('timeForStopOfCharge', Time().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 9))),
    namedtype.OptionalNamedType('chargeableDuration', Time().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 10))),
    namedtype.OptionalNamedType('interruptionTime', Time().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 11))),
    namedtype.OptionalNamedType('tariffClass', TariffClass().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 12))),
    namedtype.OptionalNamedType('tariffSwitchInd', TariffSwitchInd().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 13))),
    namedtype.OptionalNamedType('exchangeIdentity', ExchangeIdentity().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 14))),
    namedtype.OptionalNamedType('outgoingRoute', Route().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 15))),
    namedtype.OptionalNamedType('callPosition', CallPosition().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 16))),
    namedtype.OptionalNamedType('restartDuringCall', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 17))),
    namedtype.OptionalNamedType('restartDuringOutputIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 18))),
    namedtype.OptionalNamedType('lastPartialOutput', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 19))),
    namedtype.OptionalNamedType('partialOutputRecNum', PartialOutputRecNum().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 20))),
    namedtype.OptionalNamedType('cUGInterlockCode', CUGInterlockCode().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 21))),
    namedtype.OptionalNamedType('cUGIndex', CUGIndex().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 22))),
    namedtype.OptionalNamedType('presentationAndScreeningIndicator', PresentationAndScreeningIndicator().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 23))),
    namedtype.OptionalNamedType('incompleteCallDataIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 24))),
    namedtype.OptionalNamedType('networkCallReference', NetworkCallReference().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 25))),
    namedtype.OptionalNamedType('disconnectionDueToSystemRecovery', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 26))),
    namedtype.OptionalNamedType('forloppDuringOutputIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 27))),
    namedtype.OptionalNamedType('causeCode', CauseCode().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 28))),
    namedtype.OptionalNamedType('locationCode', LocationCode().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 29))),
    namedtype.OptionalNamedType('networkProvidedCallingPartyNumber', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 30))),
    namedtype.OptionalNamedType('calledPartyMNPInfo', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 31))),
    namedtype.OptionalNamedType('callingPartyNumberSpecialArrangementInd', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 32))),
    namedtype.OptionalNamedType('userProvidedCallingPartyNumber', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 33))),
    namedtype.OptionalNamedType('forloppReleaseDuringCall', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 34))),
    namedtype.OptionalNamedType('chargedParty', ChargedParty().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 35))),
    namedtype.OptionalNamedType('callAttemptIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 36))),
    namedtype.OptionalNamedType('flexibleCounter1', Counter().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 37))),
    namedtype.OptionalNamedType('flexibleCounter2', Counter().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 38))),
    namedtype.OptionalNamedType('flexibleCounter3', Counter().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 39))),
    namedtype.OptionalNamedType('flexibleCounter4', Counter().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 40))),
    namedtype.OptionalNamedType('flexibleCounter5', Counter().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 41))),
    namedtype.OptionalNamedType('flexibleCounter6', Counter().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 42))),
    namedtype.OptionalNamedType('flexibleCounter7', Counter().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 43))),
    namedtype.OptionalNamedType('flexibleCounter8', Counter().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 44))),
    namedtype.OptionalNamedType('callAttemptState', CallAttemptState().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 45))),
    namedtype.OptionalNamedType('typeOfSignalling', TypeOfSignalling().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 46))),
    namedtype.OptionalNamedType('typeOfCalledSubscriber', TypeOfCalledSubscriber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 47))),
    namedtype.OptionalNamedType('endToEndAccessDataMap', EndToEndAccessDataMap().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 48))),
    namedtype.OptionalNamedType('userToUserService1Information', UserToUserService1Information().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 49))),
    namedtype.OptionalNamedType('switchIdentity', SwitchIdentity().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 50))),
    namedtype.OptionalNamedType('aoCCurrencyAmountSentToUser', AoCCurrencyAmountSent().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 51))),
    namedtype.OptionalNamedType('globalCallReference', GlobalCallReference().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 52))),
    namedtype.OptionalNamedType('outputType', OutputType().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 102))),

    namedtype.OptionalNamedType('privateType195', univ.OctetString().subtype(implicitTag=tag.Tag(tag.tagClassPrivate, tag.tagFormatConstructed, 195))),
  )


class SCFChargingOutput(univ.Set):
  componentType = namedtype.NamedTypes(
    namedtype.OptionalNamedType('callIdentificationNumber', CallIDNumber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0))),
    namedtype.OptionalNamedType('exchangeIdentity', ExchangeIdentity().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1))),
    namedtype.OptionalNamedType('gSMCallReferenceNumber', GSMCallReferenceNumber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2))),
    namedtype.OptionalNamedType('restartDuringCall', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3))),
    namedtype.OptionalNamedType('restartDuringOutputIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4))),
    namedtype.OptionalNamedType('lastPartialOutput', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 5))),
    namedtype.OptionalNamedType('partialOutputRecNum', PartialOutputRecNum().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 6))),
    namedtype.OptionalNamedType('switchIdentity', SwitchIdentity().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 7))),
    namedtype.OptionalNamedType('disconnectionDueToSystemRecovery', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 8))),
    namedtype.OptionalNamedType('forloppDuringOutputIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 9))),
    namedtype.OptionalNamedType('forloppReleaseDuringCall', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 10))),
    namedtype.OptionalNamedType('recordSequenceNumber', RecordSequenceNumber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 11))),
    namedtype.OptionalNamedType('incompleteCallDataIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 12))),
    namedtype.OptionalNamedType('mSCAddress', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 13))),
    namedtype.OptionalNamedType('date', Date().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 14))),
    namedtype.OptionalNamedType('outputType', OutputType().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 102))),
  )


class ServiceSwitchEventModule(univ.Set):
  componentType = namedtype.NamedTypes(
    namedtype.OptionalNamedType('tAC', TAC().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0))),
    namedtype.OptionalNamedType('timeForEvent', Time().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1))),
    namedtype.OptionalNamedType('serviceSwitchingType', ServiceSwitchingType().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2))),
    namedtype.OptionalNamedType('incompleteCallDataIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3))),
  )


class ChargeRateChangeEventModule(univ.Set):
  componentType = namedtype.NamedTypes(
    namedtype.OptionalNamedType('tAC', TAC().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0))),
    namedtype.OptionalNamedType('timeForEvent', Time().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1))),
    namedtype.OptionalNamedType('radioChannelProperty', RadioChannelProperty().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2))),
    namedtype.OptionalNamedType('changeInitiatingParty', ChangeInitiatingParty().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3))),
    namedtype.OptionalNamedType('tariffClass', TariffClass().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4))),
    namedtype.OptionalNamedType('aIURRequested', AirInterfaceUserRate().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 7))),
    namedtype.OptionalNamedType('numberOfChannelsRequested', NumberOfChannels().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 8))),
    namedtype.OptionalNamedType('channelCodingUsed', ChannelCodings().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 9))),

    namedtype.OptionalNamedType('privateType195', univ.OctetString().subtype(implicitTag=tag.Tag(tag.tagClassPrivate, tag.tagFormatConstructed, 195))),
  )


class ISDNSSProcedure(univ.Set):
  componentType = namedtype.NamedTypes(
    namedtype.OptionalNamedType('trafficActivityCode', TrafficActivityCode().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0))),
    namedtype.OptionalNamedType('callIdentificationNumber', CallIDNumber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1))),
    namedtype.OptionalNamedType('recordSequenceNumber', RecordSequenceNumber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2))),
    namedtype.OptionalNamedType('typeOfCallingSubscriber', TypeOfCallingSubscriber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3))),
    namedtype.OptionalNamedType('dateForStartOfCharge', Date().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4))),
    namedtype.OptionalNamedType('timeForStartOfCharge', Time().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 5))),
    namedtype.OptionalNamedType('tariffClass', TariffClass().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 6))),
    namedtype.OptionalNamedType('exchangeIdentity', ExchangeIdentity().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 7))),
    namedtype.OptionalNamedType('restartDuringOutputIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 8))),
    namedtype.OptionalNamedType('incompleteCallDataIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 9))),
    namedtype.OptionalNamedType('forloppDuringOutputIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 10))),
    namedtype.OptionalNamedType('servedSubscriberNumber', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 11))),
    namedtype.OptionalNamedType('chargedParty', ChargedParty().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 12))),
    namedtype.OptionalNamedType('switchIdentity', SwitchIdentity().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 13))),
    namedtype.OptionalNamedType('outputType', OutputType().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 102))),

    namedtype.OptionalNamedType('privateType195', univ.OctetString().subtype(implicitTag=tag.Tag(tag.tagClassPrivate, tag.tagFormatConstructed, 195))),
  )


class IMEI(TBCDString):
  subtypeSpec = TBCDString.subtypeSpec + constraint.ValueSizeConstraint(8, 8)


class ISDNCallForwarding(univ.Set):
  componentType = namedtype.NamedTypes(
    namedtype.OptionalNamedType('trafficActivityCode', TrafficActivityCode().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0))),
    namedtype.OptionalNamedType('callIdentificationNumber', CallIDNumber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1))),
    namedtype.OptionalNamedType('recordSequenceNumber', RecordSequenceNumber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2))),
    namedtype.OptionalNamedType('typeOfCallingSubscriber', TypeOfCallingSubscriber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3))),
    namedtype.OptionalNamedType('chargedCallingPartyNumber', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4))),
    namedtype.OptionalNamedType('calledPartyNumber', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 5))),
    namedtype.OptionalNamedType('disconnectingParty', DisconnectingParty().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 6))),
    namedtype.OptionalNamedType('dateForStartOfCharge', Date().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 7))),
    namedtype.OptionalNamedType('timeForStartOfCharge', Time().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 8))),
    namedtype.OptionalNamedType('timeForStopOfCharge', Time().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 9))),
    namedtype.OptionalNamedType('chargeableDuration', Time().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 10))),
    namedtype.OptionalNamedType('interruptionTime', Time().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 11))),
    namedtype.OptionalNamedType('tariffClass', TariffClass().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 12))),
    namedtype.OptionalNamedType('tariffSwitchInd', TariffSwitchInd().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 13))),
    namedtype.OptionalNamedType('exchangeIdentity', ExchangeIdentity().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 14))),
    namedtype.OptionalNamedType('outgoingRoute', Route().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 15))),
    namedtype.OptionalNamedType('callPosition', CallPosition().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 16))),
    namedtype.OptionalNamedType('originalCalledNumber', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 17))),
    namedtype.OptionalNamedType('redirectingNumber', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 18))),
    namedtype.OptionalNamedType('restartDuringCall', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 19))),
    namedtype.OptionalNamedType('restartDuringOutputIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 20))),
    namedtype.OptionalNamedType('lastPartialOutput', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 21))),
    namedtype.OptionalNamedType('partialOutputRecNum', PartialOutputRecNum().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 22))),
    namedtype.OptionalNamedType('cUGInterlockCode', CUGInterlockCode().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 23))),
    namedtype.OptionalNamedType('cUGIndex', CUGIndex().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 24))),
    namedtype.OptionalNamedType('presentationAndScreeningIndicator', PresentationAndScreeningIndicator().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 25))),
    namedtype.OptionalNamedType('incompleteCallDataIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 26))),
    namedtype.OptionalNamedType('networkCallReference', NetworkCallReference().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 27))),
    namedtype.OptionalNamedType('disconnectionDueToSystemRecovery', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 28))),
    namedtype.OptionalNamedType('forloppDuringOutputIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 29))),
    namedtype.OptionalNamedType('causeCode', CauseCode().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 30))),
    namedtype.OptionalNamedType('locationCode', LocationCode().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 31))),
    namedtype.OptionalNamedType('networkProvidedCallingPartyNumber', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 32))),
    namedtype.OptionalNamedType('callingPartyNumber', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 33))),
    namedtype.OptionalNamedType('calledPartyMNPInfo', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 34))),
    namedtype.OptionalNamedType('forloppReleaseDuringCall', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 35))),
    namedtype.OptionalNamedType('chargedParty', ChargedParty().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 36))),
    namedtype.OptionalNamedType('callAttemptIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 37))),
    namedtype.OptionalNamedType('flexibleCounter1', Counter().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 38))),
    namedtype.OptionalNamedType('flexibleCounter2', Counter().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 39))),
    namedtype.OptionalNamedType('flexibleCounter3', Counter().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 40))),
    namedtype.OptionalNamedType('flexibleCounter4', Counter().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 41))),
    namedtype.OptionalNamedType('flexibleCounter5', Counter().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 42))),
    namedtype.OptionalNamedType('flexibleCounter6', Counter().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 43))),
    namedtype.OptionalNamedType('flexibleCounter7', Counter().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 44))),
    namedtype.OptionalNamedType('flexibleCounter8', Counter().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 45))),
    namedtype.OptionalNamedType('callAttemptState', CallAttemptState().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 46))),
    namedtype.OptionalNamedType('typeOfSignalling', TypeOfSignalling().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 47))),
    namedtype.OptionalNamedType('typeOfCalledSubscriber', TypeOfCalledSubscriber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 48))),
    namedtype.OptionalNamedType('endToEndAccessDataMap', EndToEndAccessDataMap().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 49))),
    namedtype.OptionalNamedType('userToUserService1Information', UserToUserService1Information().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 50))),
    namedtype.OptionalNamedType('switchIdentity', SwitchIdentity().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 51))),
    namedtype.OptionalNamedType('aoCCurrencyAmountSentToUser', AoCCurrencyAmountSent().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 52))),
    namedtype.OptionalNamedType('globalCallReference', GlobalCallReference().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 53))),
    namedtype.OptionalNamedType('outputType', OutputType().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 102))),

    namedtype.OptionalNamedType('privateType195', univ.OctetString().subtype(implicitTag=tag.Tag(tag.tagClassPrivate, tag.tagFormatConstructed, 195))),
  )


class ProcedureCode(TBCDString):
  subtypeSpec = TBCDString.subtypeSpec + constraint.ValueSizeConstraint(1, 1)


class MSTerminating(univ.Set):
  componentType = namedtype.NamedTypes(
    namedtype.OptionalNamedType('tAC', TAC().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0))),
    namedtype.OptionalNamedType('callIdentificationNumber', CallIDNumber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1))),
    namedtype.OptionalNamedType('recordSequenceNumber', RecordSequenceNumber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2))),
    namedtype.OptionalNamedType('typeOfCallingSubscriber', TypeOfCallingSubscriber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3))),
    namedtype.OptionalNamedType('callingPartyNumber', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4))),
    namedtype.OptionalNamedType('calledPartyNumber', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 5))),
    namedtype.OptionalNamedType('calledSubscriberIMSI', IMSI().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 6))),
    namedtype.OptionalNamedType('calledSubscriberIMEI', IMEI().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 7))),
    namedtype.OptionalNamedType('mobileStationRoamingNumber', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 8))),
    namedtype.OptionalNamedType('disconnectingParty', DisconnectingParty().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 9))),
    namedtype.OptionalNamedType('dateForStartOfCharge', Date().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 10))),
    namedtype.OptionalNamedType('timeForStartOfCharge', Time().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 11))),
    namedtype.OptionalNamedType('timeForStopOfCharge', Time().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 12))),
    namedtype.OptionalNamedType('chargeableDuration', Time().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 13))),
    namedtype.OptionalNamedType('interruptionTime', Time().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 14))),
    namedtype.OptionalNamedType('timeFromRegisterSeizureToStartOfCharging', Time().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 15))),
    namedtype.OptionalNamedType('chargedParty', ChargedParty().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 16))),
    namedtype.OptionalNamedType('originForCharging', ChargingOrigin().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 17))),
    namedtype.OptionalNamedType('tariffClass', TariffClass().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 18))),
    namedtype.OptionalNamedType('tariffSwitchInd', TariffSwitchInd().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 19))),
    namedtype.OptionalNamedType('exchangeIdentity', ExchangeIdentity().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 20))),
    namedtype.OptionalNamedType('mSCIdentification', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 21))),
    namedtype.OptionalNamedType('outgoingRoute', Route().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 22))),
    namedtype.OptionalNamedType('incomingRoute', Route().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 23))),
    namedtype.OptionalNamedType('channelAllocationPriorityLevel', ChannelAllocationPriorityLevel().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 24))),
    namedtype.OptionalNamedType('terminatingLocationNumber', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 25))),
    namedtype.OptionalNamedType('timeForTCSeizureCalled', Time().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 26))),
    namedtype.OptionalNamedType('firstCalledLocationInformation', LocationInformation().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 27))),
    namedtype.OptionalNamedType('lastCalledLocationInformation', LocationInformation().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 28))),
    namedtype.OptionalNamedType('teleServiceCode', TeleServiceCode().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 29))),
    namedtype.OptionalNamedType('bearerServiceCode', BearerServiceCode().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 30))),
    namedtype.OptionalNamedType('transparencyIndicator', TransparencyIndicator().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 31))),
    namedtype.OptionalNamedType('firstRadioChannelUsed', FirstRadioChannelUsed().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 32))),
    namedtype.OptionalNamedType('callPosition', CallPosition().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 33))),
    namedtype.OptionalNamedType('eosInfo', EosInfo().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 34))),
    namedtype.OptionalNamedType('internalCauseAndLoc', InternalCauseAndLoc().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 35))),
    namedtype.OptionalNamedType('originalCalledNumber', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 36))),
    namedtype.OptionalNamedType('redirectingNumber', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 37))),
    namedtype.OptionalNamedType('redirectionCounter', RedirectionCounter().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 38))),
    namedtype.OptionalNamedType('selectedCodec', SelectedCodec().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 39))),
    namedtype.OptionalNamedType('userToUserInformation', UserToUserInformation().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 40))),
    namedtype.OptionalNamedType('restartDuringCall', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 41))),
    namedtype.OptionalNamedType('restartDuringOutputIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 42))),
    namedtype.OptionalNamedType('dTMFUsed', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 43))),
    namedtype.OptionalNamedType('iCIOrdered', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 44))),
    namedtype.OptionalNamedType('outputForSubscriber', OutputForSubscriber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 45))),
    namedtype.OptionalNamedType('lastPartialOutput', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 46))),
    namedtype.OptionalNamedType('partialOutputRecNum', PartialOutputRecNum().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 47))),
    namedtype.OptionalNamedType('relatedCallNumber', CallIDNumber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 48))),
    namedtype.OptionalNamedType('acceptanceOfCallWaiting', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 49))),
    namedtype.OptionalNamedType('miscellaneousInformation', MiscellaneousInformation().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 50))),
    namedtype.OptionalNamedType('cUGInterlockCode', CUGInterlockCode().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 51))),
    namedtype.OptionalNamedType('cUGIndex', CUGIndex().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 52))),
    namedtype.OptionalNamedType('cUGIncomingAccessUsed', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 53))),
    namedtype.OptionalNamedType('regionalServiceUsed', RegionalServiceUsed().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 54))),
    namedtype.OptionalNamedType('regionDependentChargingOrigin', ChargingOrigin().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 55))),
    namedtype.OptionalNamedType('sSCode', SSCode().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 56))),
    namedtype.OptionalNamedType('presentationAndScreeningIndicator', PresentationAndScreeningIndicator().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 57))),
    namedtype.OptionalNamedType('radioChannelProperty', RadioChannelProperty().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 58))),
    namedtype.OptionalNamedType('faultCode', FaultCode().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 59))),
    namedtype.OptionalNamedType('intermediateRate', IntermediateRate().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 60))),
    namedtype.OptionalNamedType('firstAssignedSpeechCoderVersion', SpeechCoderVersion().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 61))),
    namedtype.OptionalNamedType('speechCoderPreferenceList', SpeechCoderPreferenceList().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 62))),
    namedtype.OptionalNamedType('subscriptionType', SubscriptionType().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 63))),
    namedtype.OptionalNamedType('incompleteCallDataIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 64))),
    namedtype.OptionalNamedType('mSCAddress', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 65))),
    namedtype.OptionalNamedType('switchIdentity', SwitchIdentity().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 66))),
    namedtype.OptionalNamedType('networkCallReference', NetworkCallReference().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 67))),
    namedtype.OptionalNamedType('frequencyBandSupported', FrequencyBandSupported().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 68))),
    namedtype.OptionalNamedType('disconnectionDueToSystemRecovery', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 69))),
    namedtype.OptionalNamedType('forloppDuringOutputIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 70))),
    namedtype.OptionalNamedType('forloppReleaseDuringCall', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 71))),
    namedtype.OptionalNamedType('accountCode', AccountCode().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 72))),
    namedtype.OptionalNamedType('gSMCallReferenceNumber', GSMCallReferenceNumber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 73))),
    namedtype.OptionalNamedType('eMLPPPriorityLevel', EMLPPPriorityLevel().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 74))),
    namedtype.OptionalNamedType('positionAccuracy', PositionAccuracy().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 75))),
    namedtype.OptionalNamedType('userTerminalPosition', UserTerminalPosition().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 76))),
    namedtype.OptionalNamedType('acceptableChannelCodings', ChannelCodings().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 77))),
    namedtype.OptionalNamedType('outgoingAssignedRoute', Route().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 78))),
    namedtype.OptionalNamedType('channelCodingUsed', ChannelCodings().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 79))),
    namedtype.OptionalNamedType('multimediaCall', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 80))),
    namedtype.OptionalNamedType('gsmSCFAddress', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 81))),
    namedtype.OptionalNamedType('fNURRequested', FixedNetworkUserRate().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 82))),
    namedtype.OptionalNamedType('aIURRequested', AirInterfaceUserRate().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 83))),
    namedtype.OptionalNamedType('numberOfChannelsRequested', NumberOfChannels().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 84))),
    namedtype.OptionalNamedType('bSSMAPCauseCode', BSSMAPCauseCode().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 85))),
    namedtype.OptionalNamedType('guaranteedBitRate', BitRate().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 86))),
    namedtype.OptionalNamedType('trafficClass', TrafficClass().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 87))),
    namedtype.OptionalNamedType('rANAPCauseCode', RANAPCauseCode().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 88))),
    namedtype.OptionalNamedType('rNCidOfFirstRNC', TargetRNCid().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 89))),
    namedtype.OptionalNamedType('maxBitRateDownlink', BitRate().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 90))),
    namedtype.OptionalNamedType('maxBitRateUplink', BitRate().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 91))),
    namedtype.OptionalNamedType('transferDelay', TransferDelay().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 92))),
    namedtype.OptionalNamedType('deliveryOfErroneousSDU1', DeliveryOfErroneousSDU().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 93))),
    namedtype.OptionalNamedType('deliveryOfErroneousSDU2', DeliveryOfErroneousSDU().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 94))),
    namedtype.OptionalNamedType('deliveryOfErroneousSDU3', DeliveryOfErroneousSDU().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 95))),
    namedtype.OptionalNamedType('residualBitErrorRatio1', ErrorRatio().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 96))),
    namedtype.OptionalNamedType('residualBitErrorRatio2', ErrorRatio().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 97))),
    namedtype.OptionalNamedType('residualBitErrorRatio3', ErrorRatio().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 98))),
    namedtype.OptionalNamedType('sDUErrorRatio1', ErrorRatio().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 99))),
    namedtype.OptionalNamedType('sDUErrorRatio2', ErrorRatio().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 100))),
    namedtype.OptionalNamedType('sDUErrorRatio3', ErrorRatio().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 101))),
    namedtype.OptionalNamedType('outputType', OutputType().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 102))),
    namedtype.OptionalNamedType('aCMChargingIndicator', ChargingIndicator().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 103))),
    namedtype.OptionalNamedType('aNMChargingIndicator', ChargingIndicator().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 104))),
    namedtype.OptionalNamedType('chargeInformation', ChargeInformation().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 105))),
    namedtype.OptionalNamedType('disconnectionDate', Date().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 106))),
    namedtype.OptionalNamedType('disconnectionTime', Time().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 107))),
    namedtype.OptionalNamedType('internationalCallIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 108))),
    namedtype.OptionalNamedType('mobileUserClass1', MobileUserClass1().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 109))),
    namedtype.OptionalNamedType('mobileUserClass2', MobileUserClass2().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 110))),
    namedtype.OptionalNamedType('originatingCarrier', CarrierInfo().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 111))),
    namedtype.OptionalNamedType('originatingChargeArea', ChargeAreaCode().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 112))),
    namedtype.OptionalNamedType('terminatingCarrier', CarrierInfo().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 113))),
    namedtype.OptionalNamedType('terminatingChargeArea', ChargeAreaCode().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 114))),
    namedtype.OptionalNamedType('userClass', UserClass().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 115))),
    namedtype.OptionalNamedType('calledSubscriberIMEISV', IMEISV().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 116))),
    namedtype.OptionalNamedType('globalCallReference', GlobalCallReference().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 117))),
    namedtype.OptionalNamedType('reroutingIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 121))),
    namedtype.OptionalNamedType('invocationOfCallHold', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 122))),
    namedtype.OptionalNamedType('retrievalOfHeldCall', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 123))),

    namedtype.OptionalNamedType('privateType195', univ.OctetString().subtype(implicitTag=tag.Tag(tag.tagClassPrivate, tag.tagFormatConstructed, 195))),
  )


class SSProcedure(univ.Set):
  componentType = namedtype.NamedTypes(
    namedtype.OptionalNamedType('tAC', TAC().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0))),
    namedtype.OptionalNamedType('callIdentificationNumber', CallIDNumber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1))),
    namedtype.OptionalNamedType('recordSequenceNumber', RecordSequenceNumber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2))),
    namedtype.OptionalNamedType('typeOfCallingSubscriber', TypeOfCallingSubscriber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3))),
    namedtype.OptionalNamedType('callingPartyNumber', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4))),
    namedtype.OptionalNamedType('callingSubscriberIMSI', IMSI().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 5))),
    namedtype.OptionalNamedType('callingSubscriberIMEI', IMEI().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 6))),
    namedtype.OptionalNamedType('dateForStartOfCharge', Date().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 7))),
    namedtype.OptionalNamedType('timeForStartOfCharge', Time().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 8))),
    namedtype.OptionalNamedType('originForCharging', ChargingOrigin().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 9))),
    namedtype.OptionalNamedType('exchangeIdentity', ExchangeIdentity().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 10))),
    namedtype.OptionalNamedType('mSCIdentification', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 11))),
    namedtype.OptionalNamedType('firstCallingLocationInformation', LocationInformation().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 12))),
    namedtype.OptionalNamedType('callingSubscriberIMEISV', IMEISV().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 13))),
    namedtype.OptionalNamedType('iCIOrdered', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 15))),
    namedtype.OptionalNamedType('outputForSubscriber', OutputForSubscriber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 16))),
    namedtype.OptionalNamedType('sSCode', SSCode().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 17))),
    namedtype.OptionalNamedType('sSRequest', SSRequest().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 18))),
    namedtype.OptionalNamedType('miscellaneousInformation', MiscellaneousInformation().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 19))),
    namedtype.OptionalNamedType('regionalServiceUsed', RegionalServiceUsed().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 20))),
    namedtype.OptionalNamedType('regionDependentChargingOrigin', ChargingOrigin().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 21))),
    namedtype.OptionalNamedType('relatedCallNumber', CallIDNumber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 22))),
    namedtype.OptionalNamedType('uSSDApplicationIdentifier', ApplicationIdentifier().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 23))),
    namedtype.OptionalNamedType('uSSDServiceCode', ServiceCode().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 24))),
    namedtype.OptionalNamedType('uSSDProcedureCode', ProcedureCode().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 25))),
    namedtype.OptionalNamedType('networkInitiatedUSSDOperations', NumberOfOperations().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 26))),
    namedtype.OptionalNamedType('uSSDOperationIdentifier', OperationIdentifier().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 27))),
    namedtype.OptionalNamedType('incompleteCallDataIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 28))),
    namedtype.OptionalNamedType('restartDuringOutputIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 29))),
    namedtype.OptionalNamedType('frequencyBandSupported', FrequencyBandSupported().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 30))),
    namedtype.OptionalNamedType('forloppDuringOutputIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 31))),
    namedtype.OptionalNamedType('switchIdentity', SwitchIdentity().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 32))),
    namedtype.OptionalNamedType('networkCallReference', NetworkCallReference().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 33))),
    namedtype.OptionalNamedType('positionAccuracy', PositionAccuracy().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 34))),
    namedtype.OptionalNamedType('userTerminalPosition', UserTerminalPosition().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 35))),
    namedtype.OptionalNamedType('rNCidOfFirstRNC', TargetRNCid().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 36))),
    namedtype.OptionalNamedType('globalCallReference', GlobalCallReference().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 37))),
    namedtype.OptionalNamedType('outputType', OutputType().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 102))),

    namedtype.OptionalNamedType('privateType195', univ.OctetString().subtype(implicitTag=tag.Tag(tag.tagClassPrivate, tag.tagFormatConstructed, 195))),
  )


class RoamingCallForwarding(univ.Set):
  componentType = namedtype.NamedTypes(
    namedtype.OptionalNamedType('tAC', TAC().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0))),
    namedtype.OptionalNamedType('callIdentificationNumber', CallIDNumber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1))),
    namedtype.OptionalNamedType('recordSequenceNumber', RecordSequenceNumber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2))),
    namedtype.OptionalNamedType('typeOfCallingSubscriber', TypeOfCallingSubscriber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3))),
    namedtype.OptionalNamedType('callingPartyNumber', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4))),
    namedtype.OptionalNamedType('calledPartyNumber', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 5))),
    namedtype.OptionalNamedType('calledSubscriberIMSI', IMSI().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 6))),
    namedtype.OptionalNamedType('mobileStationRoamingNumber', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 7))),
    namedtype.OptionalNamedType('disconnectingParty', DisconnectingParty().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 8))),
    namedtype.OptionalNamedType('dateForStartOfCharge', Date().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 9))),
    namedtype.OptionalNamedType('timeForStartOfCharge', Time().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 10))),
    namedtype.OptionalNamedType('timeForStopOfCharge', Time().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 11))),
    namedtype.OptionalNamedType('chargeableDuration', Time().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 12))),
    namedtype.OptionalNamedType('interruptionTime', Time().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 13))),
    namedtype.OptionalNamedType('timeFromRegisterSeizureToStartOfCharging', Time().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 14))),
    namedtype.OptionalNamedType('chargedParty', ChargedParty().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 15))),
    namedtype.OptionalNamedType('originForCharging', ChargingOrigin().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 16))),
    namedtype.OptionalNamedType('tariffClass', TariffClass().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 17))),
    namedtype.OptionalNamedType('tariffSwitchInd', TariffSwitchInd().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 18))),
    namedtype.OptionalNamedType('exchangeIdentity', ExchangeIdentity().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 19))),
    namedtype.OptionalNamedType('mSCIdentification', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 20))),
    namedtype.OptionalNamedType('outgoingRoute', Route().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 21))),
    namedtype.OptionalNamedType('incomingRoute', Route().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 22))),
    namedtype.OptionalNamedType('miscellaneousInformation', MiscellaneousInformation().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 23))),
    namedtype.OptionalNamedType('subscriptionType', SubscriptionType().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 24))),
    namedtype.OptionalNamedType('callPosition', CallPosition().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 25))),
    namedtype.OptionalNamedType('eosInfo', EosInfo().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 26))),
    namedtype.OptionalNamedType('internalCauseAndLoc', InternalCauseAndLoc().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 27))),
    namedtype.OptionalNamedType('originalCalledNumber', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 28))),
    namedtype.OptionalNamedType('redirectingNumber', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 29))),
    namedtype.OptionalNamedType('redirectionCounter', RedirectionCounter().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 30))),
    namedtype.OptionalNamedType('restartDuringCall', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 31))),
    namedtype.OptionalNamedType('restartDuringOutputIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 32))),
    namedtype.OptionalNamedType('numberOfMeterPulses', NumberOfMeterPulses().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 33))),
    namedtype.OptionalNamedType('c7ChargingMessage', C7ChargingMessage().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 34))),
    namedtype.OptionalNamedType('c7FirstCHTMessage', C7CHTMessage().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 35))),
    namedtype.OptionalNamedType('c7SecondCHTMessage', C7CHTMessage().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 36))),
    namedtype.OptionalNamedType('iCIOrdered', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 37))),
    namedtype.OptionalNamedType('outputForSubscriber', OutputForSubscriber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 38))),
    namedtype.OptionalNamedType('lastPartialOutput', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 39))),
    namedtype.OptionalNamedType('partialOutputRecNum', PartialOutputRecNum().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 40))),
    namedtype.OptionalNamedType('relatedCallNumber', CallIDNumber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 41))),
    namedtype.OptionalNamedType('cUGInterlockCode', CUGInterlockCode().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 42))),
    namedtype.OptionalNamedType('cUGOutgoingAccessIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 43))),
    namedtype.OptionalNamedType('presentationAndScreeningIndicator', PresentationAndScreeningIndicator().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 44))),
    namedtype.OptionalNamedType('faultCode', FaultCode().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 45))),
    namedtype.OptionalNamedType('incompleteCallDataIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 46))),
    namedtype.OptionalNamedType('multimediaInformation', MultimediaInformation().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 47))),
    namedtype.OptionalNamedType('switchIdentity', SwitchIdentity().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 48))),
    namedtype.OptionalNamedType('networkCallReference', NetworkCallReference().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 49))),
    namedtype.OptionalNamedType('disconnectionDueToSystemRecovery', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 50))),
    namedtype.OptionalNamedType('forloppDuringOutputIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 51))),
    namedtype.OptionalNamedType('forloppReleaseDuringCall', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 52))),
    namedtype.OptionalNamedType('gSMCallReferenceNumber', GSMCallReferenceNumber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 53))),
    namedtype.OptionalNamedType('mSCAddress', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 54))),
    namedtype.OptionalNamedType('carrierInformationBackward', TransitCarrierInfo().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 55))),
    namedtype.OptionalNamedType('originatingAccessISDN', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 56))),
    namedtype.OptionalNamedType('originatingCarrier', CarrierInfo().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 57))),
    namedtype.OptionalNamedType('originatingChargeArea', ChargeAreaCode().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 58))),
    namedtype.OptionalNamedType('terminatingAccessISDN', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 59))),
    namedtype.OptionalNamedType('terminatingCarrier', CarrierInfo().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 60))),
    namedtype.OptionalNamedType('terminatingChargeArea', ChargeAreaCode().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 61))),
    namedtype.OptionalNamedType('contractorNumber', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 62))),
    namedtype.OptionalNamedType('carrierIdentificationCode', CarrierIdentificationCode().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 63))),
    namedtype.OptionalNamedType('carrierInformation', CarrierInformation().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 64))),
    namedtype.OptionalNamedType('carrierSelectionSubstitutionInformation', CarrierSelectionSubstitutionInformation().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 65))),
    namedtype.OptionalNamedType('chargeNumber', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 66))),
    namedtype.OptionalNamedType('interExchangeCarrierIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 67))),
    namedtype.OptionalNamedType('originatingLineInformation', OriginatingLineInformation().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 68))),
    namedtype.OptionalNamedType('userToUserInformation', UserToUserInformation().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 69))),
    namedtype.OptionalNamedType('globalCallReference', GlobalCallReference().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 70))),
    namedtype.OptionalNamedType('rTCIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 71))),
    namedtype.OptionalNamedType('rTCSessionID', RTCSessionID().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 72))),
    namedtype.OptionalNamedType('rTCDefaultServiceHandling', RTCDefaultServiceHandling().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 73))),
    namedtype.OptionalNamedType('RTCFailureIndicator', RTCFailureIndicator().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 74))),
    namedtype.OptionalNamedType('RTCNotInvokedReason', RTCNotInvokedReason().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 75))),
    namedtype.OptionalNamedType('outputType', OutputType().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 102))),
    namedtype.OptionalNamedType('reroutingIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 121))),

    namedtype.OptionalNamedType('privateType195', univ.OctetString().subtype(implicitTag=tag.Tag(tag.tagClassPrivate, tag.tagFormatConstructed, 195))),
  )


class CallForwarding(univ.Set):
  componentType = namedtype.NamedTypes(
    namedtype.OptionalNamedType('tAC', TAC().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0))),
    namedtype.OptionalNamedType('callIdentificationNumber', CallIDNumber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1))),
    namedtype.OptionalNamedType('recordSequenceNumber', RecordSequenceNumber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2))),
    namedtype.OptionalNamedType('typeOfCallingSubscriber', TypeOfCallingSubscriber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3))),
    namedtype.OptionalNamedType('callingPartyNumber', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4))),
    namedtype.OptionalNamedType('calledPartyNumber', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 5))),
    namedtype.OptionalNamedType('originalCalledNumber', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 6))),
    namedtype.OptionalNamedType('redirectingNumber', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 7))),
    namedtype.OptionalNamedType('redirectionCounter', RedirectionCounter().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 8))),
    namedtype.OptionalNamedType('redirectingSPN', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 9))),
    namedtype.OptionalNamedType('redirectingIMSI', IMSI().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 10))),
    namedtype.OptionalNamedType('mobileStationRoamingNumber', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 11))),
    namedtype.OptionalNamedType('disconnectingParty', DisconnectingParty().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 12))),
    namedtype.OptionalNamedType('dateForStartOfCharge', Date().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 13))),
    namedtype.OptionalNamedType('timeForStartOfCharge', Time().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 14))),
    namedtype.OptionalNamedType('timeForStopOfCharge', Time().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 15))),
    namedtype.OptionalNamedType('chargeableDuration', Time().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 16))),
    namedtype.OptionalNamedType('interruptionTime', Time().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 17))),
    namedtype.OptionalNamedType('timeFromRegisterSeizureToStartOfCharging', Time().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 18))),
    namedtype.OptionalNamedType('chargedParty', ChargedParty().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 19))),
    namedtype.OptionalNamedType('originForCharging', ChargingOrigin().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 20))),
    namedtype.OptionalNamedType('tariffClass', TariffClass().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 21))),
    namedtype.OptionalNamedType('tariffSwitchInd', TariffSwitchInd().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 22))),
    namedtype.OptionalNamedType('exchangeIdentity', ExchangeIdentity().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 23))),
    namedtype.OptionalNamedType('mSCIdentification', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 24))),
    namedtype.OptionalNamedType('outgoingRoute', Route().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 25))),
    namedtype.OptionalNamedType('incomingRoute', Route().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 26))),
    namedtype.OptionalNamedType('miscellaneousInformation', MiscellaneousInformation().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 27))),
    namedtype.OptionalNamedType('originatingLocationNumber', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 28))),
    namedtype.OptionalNamedType('callPosition', CallPosition().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 29))),
    namedtype.OptionalNamedType('eosInfo', EosInfo().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 30))),
    namedtype.OptionalNamedType('internalCauseAndLoc', InternalCauseAndLoc().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 31))),
    namedtype.OptionalNamedType('restartDuringCall', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 32))),
    namedtype.OptionalNamedType('restartDuringOutputIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 33))),
    namedtype.OptionalNamedType('numberOfMeterPulses', NumberOfMeterPulses().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 34))),
    namedtype.OptionalNamedType('c7ChargingMessage', C7ChargingMessage().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 35))),
    namedtype.OptionalNamedType('c7FirstCHTMessage', C7CHTMessage().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 36))),
    namedtype.OptionalNamedType('c7SecondCHTMessage', C7CHTMessage().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 37))),
    namedtype.OptionalNamedType('iCIOrdered', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 38))),
    namedtype.OptionalNamedType('outputForSubscriber', OutputForSubscriber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 39))),
    namedtype.OptionalNamedType('iNMarkingOfMS', INMarkingOfMS().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 40))),
    namedtype.OptionalNamedType('lastPartialOutput', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 41))),
    namedtype.OptionalNamedType('partialOutputRecNum', PartialOutputRecNum().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 42))),
    namedtype.OptionalNamedType('relatedCallNumber', CallIDNumber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 43))),
    namedtype.OptionalNamedType('cUGInterlockCode', CUGInterlockCode().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 44))),
    namedtype.OptionalNamedType('cUGIndex', CUGIndex().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 45))),
    namedtype.OptionalNamedType('cUGOutgoingAccessUsed', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 46))),
    namedtype.OptionalNamedType('cUGOutgoingAccessIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 47))),
    namedtype.OptionalNamedType('regionalServiceUsed', RegionalServiceUsed().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 48))),
    namedtype.OptionalNamedType('regionDependentChargingOrigin', ChargingOrigin().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 49))),
    namedtype.OptionalNamedType('presentationAndScreeningIndicator', PresentationAndScreeningIndicator().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 50))),
    namedtype.OptionalNamedType('faultCode', FaultCode().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 51))),
    namedtype.OptionalNamedType('subscriptionType', SubscriptionType().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 52))),
    namedtype.OptionalNamedType('incompleteCallDataIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 53))),
    namedtype.OptionalNamedType('incompleteCompositeCDRIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 54))),
    namedtype.OptionalNamedType('switchIdentity', SwitchIdentity().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 56))),
    namedtype.OptionalNamedType('networkCallReference', NetworkCallReference().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 57))),
    namedtype.OptionalNamedType('disconnectionDueToSystemRecovery', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 58))),
    namedtype.OptionalNamedType('forloppDuringOutputIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 59))),
    namedtype.OptionalNamedType('forloppReleaseDuringCall', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 60))),
    namedtype.OptionalNamedType('translatedNumber', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 61))),
    namedtype.OptionalNamedType('cAMELInitiatedCallForwarding', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 62))),
    namedtype.OptionalNamedType('bCSMTDPData1', CAMELTDPData().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 63))),
    namedtype.OptionalNamedType('bCSMTDPData2', CAMELTDPData().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 64))),
    namedtype.OptionalNamedType('bCSMTDPData3', CAMELTDPData().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 65))),
    namedtype.OptionalNamedType('bCSMTDPData4', CAMELTDPData().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 66))),
    namedtype.OptionalNamedType('bCSMTDPData5', CAMELTDPData().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 67))),
    namedtype.OptionalNamedType('bCSMTDPData6', CAMELTDPData().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 68))),
    namedtype.OptionalNamedType('bCSMTDPData7', CAMELTDPData().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 69))),
    namedtype.OptionalNamedType('bCSMTDPData8', CAMELTDPData().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 70))),
    namedtype.OptionalNamedType('bCSMTDPData9', CAMELTDPData().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 71))),
    namedtype.OptionalNamedType('bCSMTDPData10', CAMELTDPData().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 72))),
    namedtype.OptionalNamedType('gSMCallReferenceNumber', GSMCallReferenceNumber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 73))),
    namedtype.OptionalNamedType('mSCAddress', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 74))),
    namedtype.OptionalNamedType('aCMChargingIndicator', ChargingIndicator().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 75))),
    namedtype.OptionalNamedType('aNMChargingIndicator', ChargingIndicator().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 76))),
    namedtype.OptionalNamedType('carrierInformationBackward', TransitCarrierInfo().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 77))),
    namedtype.OptionalNamedType('chargeInformation', ChargeInformation().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 78))),
    namedtype.OptionalNamedType('disconnectionDate', Date().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 79))),
    namedtype.OptionalNamedType('disconnectionTime', Time().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 80))),
    namedtype.OptionalNamedType('exitPOICA', ChargeAreaCode().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 81))),
    namedtype.OptionalNamedType('originatingCarrier', CarrierInfo().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 82))),
    namedtype.OptionalNamedType('originatingChargeArea', ChargeAreaCode().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 83))),
    namedtype.OptionalNamedType('terminatingAccessISDN', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 84))),
    namedtype.OptionalNamedType('terminatingCarrier', CarrierInfo().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 85))),
    namedtype.OptionalNamedType('terminatingChargeArea', ChargeAreaCode().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 86))),
    namedtype.OptionalNamedType('terminatingMobileUserClass1', MobileUserClass1().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 87))),
    namedtype.OptionalNamedType('terminatingMobileUserClass2', MobileUserClass2().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 88))),
    namedtype.OptionalNamedType('terminatingUserClass', UserClass().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 89))),
    namedtype.OptionalNamedType('originatingAccessISDN', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 90))),
    namedtype.OptionalNamedType('contractorNumber', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 91))),
    namedtype.OptionalNamedType('calledPartyMNPInfo', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 92))),
    namedtype.OptionalNamedType('carrierIdentificationCode', CarrierIdentificationCode().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 93))),
    namedtype.OptionalNamedType('carrierInformation', CarrierInformation().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 94))),
    namedtype.OptionalNamedType('carrierSelectionSubstitutionInformation', CarrierSelectionSubstitutionInformation().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 95))),
    namedtype.OptionalNamedType('chargeNumber', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 96))),
    namedtype.OptionalNamedType('interExchangeCarrierIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 97))),
    namedtype.OptionalNamedType('originatingLineInformation', OriginatingLineInformation().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 98))),
    namedtype.OptionalNamedType('optimalRoutingType', OptimalRoutingType().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 99))),
    namedtype.OptionalNamedType('optimalRoutingInvocationFailed', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 100))),
    namedtype.OptionalNamedType('userToUserInformation', UserToUserInformation().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 101))),
    namedtype.OptionalNamedType('outputType', OutputType().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 102))),
    namedtype.OptionalNamedType('multimediaInformation', MultimediaInformation().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 103))),
    namedtype.OptionalNamedType('globalCallReference', GlobalCallReference().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 104))),
    namedtype.OptionalNamedType('rTCIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 105))),
    namedtype.OptionalNamedType('rTCSessionID', RTCSessionID().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 106))),
    namedtype.OptionalNamedType('rTCDefaultServiceHandling', RTCDefaultServiceHandling().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 107))),
    namedtype.OptionalNamedType('rTCFailureIndicator', RTCFailureIndicator().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 108))),
    namedtype.OptionalNamedType('rTCNotInvokedReason', RTCNotInvokedReason().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 109))),
    namedtype.OptionalNamedType('originatedCode', OriginatedCode().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 55))),
    namedtype.OptionalNamedType('reroutingIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 121))),

    namedtype.OptionalNamedType('privateType195', univ.OctetString().subtype(implicitTag=tag.Tag(tag.tagClassPrivate, tag.tagFormatConstructed, 195))),
  )


class Transit(univ.Set):
  componentType = namedtype.NamedTypes(
    namedtype.OptionalNamedType('tAC', TAC().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0))),
    namedtype.OptionalNamedType('callIdentificationNumber', CallIDNumber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1))),
    namedtype.OptionalNamedType('recordSequenceNumber', RecordSequenceNumber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2))),
    namedtype.OptionalNamedType('typeOfCallingSubscriber', TypeOfCallingSubscriber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3))),
    namedtype.OptionalNamedType('callingPartyNumber', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4))),
    namedtype.OptionalNamedType('calledPartyNumber', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 5))),
    namedtype.OptionalNamedType('calledSubscriberIMSI', IMSI().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 6))),
    namedtype.OptionalNamedType('disconnectingParty', DisconnectingParty().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 7))),
    namedtype.OptionalNamedType('dateForStartOfCharge', Date().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 8))),
    namedtype.OptionalNamedType('timeForStartOfCharge', Time().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 9))),
    namedtype.OptionalNamedType('timeForStopOfCharge', Time().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 10))),
    namedtype.OptionalNamedType('chargeableDuration', Time().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 11))),
    namedtype.OptionalNamedType('interruptionTime', Time().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 12))),
    namedtype.OptionalNamedType('timeFromRegisterSeizureToStartOfCharging', Time().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 13))),
    namedtype.OptionalNamedType('chargedParty', ChargedParty().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 14))),
    namedtype.OptionalNamedType('originForCharging', ChargingOrigin().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 15))),
    namedtype.OptionalNamedType('tariffClass', TariffClass().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 16))),
    namedtype.OptionalNamedType('tariffSwitchInd', TariffSwitchInd().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 17))),
    namedtype.OptionalNamedType('numberOfMeterPulses', NumberOfMeterPulses().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 18))),
    namedtype.OptionalNamedType('exchangeIdentity', ExchangeIdentity().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 19))),
    namedtype.OptionalNamedType('mSCIdentification', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 20))),
    namedtype.OptionalNamedType('outgoingRoute', Route().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 21))),
    namedtype.OptionalNamedType('incomingRoute', Route().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 22))),
    namedtype.OptionalNamedType('miscellaneousInformation', MiscellaneousInformation().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 23))),
    namedtype.OptionalNamedType('iNMarkingOfMS', INMarkingOfMS().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 25))),
    namedtype.OptionalNamedType('callPosition', CallPosition().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 26))),
    namedtype.OptionalNamedType('eosInfo', EosInfo().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 27))),
    namedtype.OptionalNamedType('internalCauseAndLoc', InternalCauseAndLoc().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 28))),
    namedtype.OptionalNamedType('originalCalledNumber', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 29))),
    namedtype.OptionalNamedType('redirectingNumber', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 30))),
    namedtype.OptionalNamedType('redirectionCounter', RedirectionCounter().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 31))),
    namedtype.OptionalNamedType('redirectingDropBackNumber', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 32))),
    namedtype.OptionalNamedType('redirectingDropBack', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 33))),
    namedtype.OptionalNamedType('restartDuringCall', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 34))),
    namedtype.OptionalNamedType('restartDuringOutputIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 35))),
    namedtype.OptionalNamedType('iCIOrdered', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 36))),
    namedtype.OptionalNamedType('outputForSubscriber', OutputForSubscriber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 37))),
    namedtype.OptionalNamedType('lastPartialOutput', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 38))),
    namedtype.OptionalNamedType('partialOutputRecNum', PartialOutputRecNum().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 39))),
    namedtype.OptionalNamedType('relatedCallNumber', CallIDNumber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 40))),
    namedtype.OptionalNamedType('faultCode', FaultCode().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 41))),
    namedtype.OptionalNamedType('subscriptionType', SubscriptionType().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 42))),
    namedtype.OptionalNamedType('incompleteCallDataIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 43))),
    namedtype.OptionalNamedType('incompleteCompositeCDRIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 44))),
    namedtype.OptionalNamedType('switchIdentity', SwitchIdentity().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 45))),
    namedtype.OptionalNamedType('networkCallReference', NetworkCallReference().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 46))),
    namedtype.OptionalNamedType('disconnectionDueToSystemRecovery', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 47))),
    namedtype.OptionalNamedType('forloppDuringOutputIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 48))),
    namedtype.OptionalNamedType('forloppReleaseDuringCall', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 49))),
    namedtype.OptionalNamedType('translatedNumber', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 50))),
    namedtype.OptionalNamedType('bCSMTDPData1', CAMELTDPData().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 51))),
    namedtype.OptionalNamedType('bCSMTDPData2', CAMELTDPData().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 52))),
    namedtype.OptionalNamedType('bCSMTDPData3', CAMELTDPData().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 53))),
    namedtype.OptionalNamedType('bCSMTDPData4', CAMELTDPData().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 54))),
    namedtype.OptionalNamedType('bCSMTDPData5', CAMELTDPData().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 55))),
    namedtype.OptionalNamedType('bCSMTDPData6', CAMELTDPData().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 56))),
    namedtype.OptionalNamedType('bCSMTDPData7', CAMELTDPData().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 57))),
    namedtype.OptionalNamedType('bCSMTDPData8', CAMELTDPData().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 58))),
    namedtype.OptionalNamedType('bCSMTDPData9', CAMELTDPData().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 59))),
    namedtype.OptionalNamedType('bCSMTDPData10', CAMELTDPData().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 60))),
    namedtype.OptionalNamedType('gSMCallReferenceNumber', GSMCallReferenceNumber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 61))),
    namedtype.OptionalNamedType('c7ChargingMessage', C7ChargingMessage().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 62))),
    namedtype.OptionalNamedType('c7FirstCHTMessage', C7CHTMessage().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 63))),
    namedtype.OptionalNamedType('c7SecondCHTMessage', C7CHTMessage().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 64))),
    namedtype.OptionalNamedType('aCMChargingIndicator', ChargingIndicator().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 65))),
    namedtype.OptionalNamedType('aNMChargingIndicator', ChargingIndicator().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 66))),
    namedtype.OptionalNamedType('mSCAddress', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 67))),
    namedtype.OptionalNamedType('carrierInformationBackward', TransitCarrierInfo().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 68))),
    namedtype.OptionalNamedType('carrierInformationForward', TransitCarrierInfo().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 69))),
    namedtype.OptionalNamedType('chargeInformation', ChargeInformation().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 70))),
    namedtype.OptionalNamedType('disconnectionDate', Date().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 71))),
    namedtype.OptionalNamedType('disconnectionTime', Time().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 72))),
    namedtype.OptionalNamedType('entryPOICA', ChargeAreaCode().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 73))),
    namedtype.OptionalNamedType('exitPOICA', ChargeAreaCode().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 74))),
    namedtype.OptionalNamedType('internationalCallIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 75))),
    namedtype.OptionalNamedType('mobileUserClass1', MobileUserClass1().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 76))),
    namedtype.OptionalNamedType('mobileUserClass2', MobileUserClass2().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 77))),
    namedtype.OptionalNamedType('originatingAccessISDN', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 78))),
    namedtype.OptionalNamedType('originatingCarrier', CarrierInfo().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 79))),
    namedtype.OptionalNamedType('originatingChargeArea', ChargeAreaCode().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 80))),
    namedtype.OptionalNamedType('tDSCounter', Counter().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 81))),
    namedtype.OptionalNamedType('terminatingAccessISDN', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 82))),
    namedtype.OptionalNamedType('terminatingCarrier', CarrierInfo().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 83))),
    namedtype.OptionalNamedType('terminatingChargeArea', ChargeAreaCode().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 84))),
    namedtype.OptionalNamedType('terminatingMobileUserClass1', MobileUserClass1().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 85))),
    namedtype.OptionalNamedType('terminatingMobileUserClass2', MobileUserClass2().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 86))),
    namedtype.OptionalNamedType('contractorNumber', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 87))),
    namedtype.OptionalNamedType('terminatingUserClass', UserClass().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 88))),
    namedtype.OptionalNamedType('userClass', UserClass().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 89))),
    namedtype.OptionalNamedType('calledPartyMNPInfo', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 90))),
    namedtype.OptionalNamedType('chargeNumber', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 91))),
    namedtype.OptionalNamedType('originatingLineInformation', OriginatingLineInformation().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 92))),
    namedtype.OptionalNamedType('multimediaInformation', MultimediaInformation().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 93))),
    namedtype.OptionalNamedType('globalCallReference', GlobalCallReference().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 94))),
    namedtype.OptionalNamedType('rTCIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 95))),
    namedtype.OptionalNamedType('rTCSessionID', RTCSessionID().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 96))),
    namedtype.OptionalNamedType('rTCDefaultServiceHandling', RTCDefaultServiceHandling().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 97))),
    namedtype.OptionalNamedType('rTCFailureIndicator', RTCFailureIndicator().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 98))),
    namedtype.OptionalNamedType('rTCNotInvokedReason', RTCNotInvokedReason().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 99))),
    namedtype.OptionalNamedType('outputType', OutputType().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 102))),
    namedtype.OptionalNamedType('originatedCode', OriginatedCode().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 24))),
    namedtype.OptionalNamedType('reroutingIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 121))),

    namedtype.OptionalNamedType('privateType195', univ.OctetString().subtype(implicitTag=tag.Tag(tag.tagClassPrivate, tag.tagFormatConstructed, 195))),
  )


class MSOriginatingSMSinMSC(univ.Set):
  componentType = namedtype.NamedTypes(
    namedtype.OptionalNamedType('tAC', TAC().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0))),
    namedtype.OptionalNamedType('callIdentificationNumber', CallIDNumber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1))),
    namedtype.OptionalNamedType('recordSequenceNumber', RecordSequenceNumber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2))),
    namedtype.OptionalNamedType('typeOfCallingSubscriber', TypeOfCallingSubscriber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3))),
    namedtype.OptionalNamedType('callingPartyNumber', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4))),
    namedtype.OptionalNamedType('callingSubscriberIMSI', IMSI().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 5))),
    namedtype.OptionalNamedType('callingSubscriberIMEI', IMEI().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 6))),
    namedtype.OptionalNamedType('dateForStartOfCharge', Date().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 7))),
    namedtype.OptionalNamedType('timeForStartOfCharge', Time().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 8))),
    namedtype.OptionalNamedType('chargedParty', ChargedParty().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 9))),
    namedtype.OptionalNamedType('originForCharging', ChargingOrigin().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 10))),
    namedtype.OptionalNamedType('exchangeIdentity', ExchangeIdentity().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 11))),
    namedtype.OptionalNamedType('mSCIdentification', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 12))),
    namedtype.OptionalNamedType('incomingRoute', Route().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 13))),
    namedtype.OptionalNamedType('firstCallingLocationInformation', LocationInformation().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 14))),
    namedtype.OptionalNamedType('teleServiceCode', TeleServiceCode().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 15))),
    namedtype.OptionalNamedType('serviceCentreAddress', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 16))),
    namedtype.OptionalNamedType('callingSubscriberIMEISV', IMEISV().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 17))),
    namedtype.OptionalNamedType('iCIOrdered', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 19))),
    namedtype.OptionalNamedType('outputForSubscriber', OutputForSubscriber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 20))),
    namedtype.OptionalNamedType('miscellaneousInformation', MiscellaneousInformation().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 21))),
    namedtype.OptionalNamedType('regionalServiceUsed', RegionalServiceUsed().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 22))),
    namedtype.OptionalNamedType('regionDependentChargingOrigin', ChargingOrigin().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 23))),
    namedtype.OptionalNamedType('channelAllocationPriorityLevel', ChannelAllocationPriorityLevel().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 24))),
    namedtype.OptionalNamedType('frequencyBandSupported', FrequencyBandSupported().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 25))),
    namedtype.OptionalNamedType('incompleteCallDataIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 26))),
    namedtype.OptionalNamedType('restartDuringOutputIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 27))),
    namedtype.OptionalNamedType('forloppDuringOutputIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 28))),
    namedtype.OptionalNamedType('positionAccuracy', PositionAccuracy().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 29))),
    namedtype.OptionalNamedType('userTerminalPosition', UserTerminalPosition().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 30))),
    namedtype.OptionalNamedType('switchIdentity', SwitchIdentity().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 31))),
    namedtype.OptionalNamedType('destinationAddress', AddressStringExtended().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 32))),
    namedtype.OptionalNamedType('messageReference', MessageReference().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 33))),
    namedtype.OptionalNamedType('messageTypeIndicator', MessageTypeIndicator().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 34))),
    namedtype.OptionalNamedType('rNCidOfFirstRNC', TargetRNCid().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 35))),
    namedtype.OptionalNamedType('bCSMTDPData1', CAMELTDPData().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 36))),
    namedtype.OptionalNamedType('cAMELCallingPartyNumber', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 37))),
    namedtype.OptionalNamedType('cAMELDestinationAddress', AddressStringExtended().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 38))),
    namedtype.OptionalNamedType('cAMELSMSCAddress', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 39))),
    namedtype.OptionalNamedType('defaultSMSHandling', DefaultSMS_Handling().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 40))),
    namedtype.OptionalNamedType('freeFormatData', FreeFormatData().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 41))),
    namedtype.OptionalNamedType('sMSResult', SMSResult().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 42))),
    namedtype.OptionalNamedType('sMSReferenceNumber', GSMCallReferenceNumber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 43))),
    namedtype.OptionalNamedType('mSCAddress', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 44))),
    namedtype.OptionalNamedType('rTCIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 45))),
    namedtype.OptionalNamedType('rTCSessionID', RTCSessionID().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 46))),
    namedtype.OptionalNamedType('rTCDefaultServiceHandling', RTCDefaultServiceHandling().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 47))),
    namedtype.OptionalNamedType('rTCFailureIndicator', RTCFailureIndicator().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 48))),
    namedtype.OptionalNamedType('rTCNotInvokedReason', RTCNotInvokedReason().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 49))),
    namedtype.OptionalNamedType('outputType', OutputType().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 102))),

    namedtype.OptionalNamedType('privateType195', univ.OctetString().subtype(implicitTag=tag.Tag(tag.tagClassPrivate, tag.tagFormatConstructed, 195))),
  )


class MSOriginating(univ.Set):
  componentType = namedtype.NamedTypes(
    namedtype.OptionalNamedType('tAC', TAC().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0))),
    namedtype.OptionalNamedType('callIdentificationNumber', CallIDNumber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1))),
    namedtype.OptionalNamedType('recordSequenceNumber', RecordSequenceNumber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2))),
    namedtype.OptionalNamedType('typeOfCallingSubscriber', TypeOfCallingSubscriber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3))),
    namedtype.OptionalNamedType('callingPartyNumber', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4))),
    namedtype.OptionalNamedType('callingSubscriberIMSI', IMSI().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 5))),
    namedtype.OptionalNamedType('callingSubscriberIMEI', IMEI().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 6))),
    namedtype.OptionalNamedType('calledPartyNumber', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 7))),
    namedtype.OptionalNamedType('disconnectingParty', DisconnectingParty().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 8))),
    namedtype.OptionalNamedType('dateForStartOfCharge', Date().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 9))),
    namedtype.OptionalNamedType('timeForStartOfCharge', Time().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 10))),
    namedtype.OptionalNamedType('timeForStopOfCharge', Time().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 11))),
    namedtype.OptionalNamedType('chargeableDuration', Time().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 12))),
    namedtype.OptionalNamedType('interruptionTime', Time().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 13))),
    namedtype.OptionalNamedType('timeFromRegisterSeizureToStartOfCharging', Time().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 14))),
    namedtype.OptionalNamedType('chargedParty', ChargedParty().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 15))),
    namedtype.OptionalNamedType('originForCharging', ChargingOrigin().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 16))),
    namedtype.OptionalNamedType('chargingCase', ChargingCase().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 17))),
    namedtype.OptionalNamedType('tariffClass', TariffClass().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 18))),
    namedtype.OptionalNamedType('tariffSwitchInd', TariffSwitchInd().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 19))),
    namedtype.OptionalNamedType('exchangeIdentity', ExchangeIdentity().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 20))),
    namedtype.OptionalNamedType('mSCIdentification', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 21))),
    namedtype.OptionalNamedType('outgoingRoute', Route().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 22))),
    namedtype.OptionalNamedType('incomingRoute', Route().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 23))),
    namedtype.OptionalNamedType('miscellaneousInformation', MiscellaneousInformation().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 24))),
    namedtype.OptionalNamedType('originatingLocationNumber', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 25))),
    namedtype.OptionalNamedType('timeForTCSeizureCalling', Time().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 26))),
    namedtype.OptionalNamedType('firstCallingLocationInformation', LocationInformation().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 27))),
    namedtype.OptionalNamedType('lastCallingLocationInformation', LocationInformation().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 28))),
    namedtype.OptionalNamedType('teleServiceCode', TeleServiceCode().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 29))),
    namedtype.OptionalNamedType('bearerServiceCode', BearerServiceCode().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 30))),
    namedtype.OptionalNamedType('transparencyIndicator', TransparencyIndicator().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 31))),
    namedtype.OptionalNamedType('firstRadioChannelUsed', FirstRadioChannelUsed().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 32))),
    namedtype.OptionalNamedType('callPosition', CallPosition().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 33))),
    namedtype.OptionalNamedType('eosInfo', EosInfo().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 34))),
    namedtype.OptionalNamedType('internalCauseAndLoc', InternalCauseAndLoc().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 35))),
    namedtype.OptionalNamedType('restartDuringCall', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 36))),
    namedtype.OptionalNamedType('restartDuringOutputIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 37))),
    namedtype.OptionalNamedType('numberOfMeterPulses', NumberOfMeterPulses().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 38))),
    namedtype.OptionalNamedType('c7ChargingMessage', C7ChargingMessage().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 39))),
    namedtype.OptionalNamedType('c7FirstCHTMessage', C7CHTMessage().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 40))),
    namedtype.OptionalNamedType('c7SecondCHTMessage', C7CHTMessage().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 41))),
    namedtype.OptionalNamedType('calledPartyMNPInfo', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 42))),
    namedtype.OptionalNamedType('carrierIdentificationCode', CarrierIdentificationCode().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 43))),
    namedtype.OptionalNamedType('dTMFUsed', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 44))),
    namedtype.OptionalNamedType('iCIOrdered', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 45))),
    namedtype.OptionalNamedType('outputForSubscriber', OutputForSubscriber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 46))),
    namedtype.OptionalNamedType('iNMarkingOfMS', INMarkingOfMS().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 47))),
    namedtype.OptionalNamedType('lastPartialOutput', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 48))),
    namedtype.OptionalNamedType('partialOutputRecNum', PartialOutputRecNum().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 49))),
    namedtype.OptionalNamedType('cUGInterlockCode', CUGInterlockCode().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 50))),
    namedtype.OptionalNamedType('cUGIndex', CUGIndex().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 51))),
    namedtype.OptionalNamedType('cUGOutgoingAccessUsed', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 52))),
    namedtype.OptionalNamedType('cUGOutgoingAccessIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 53))),
    namedtype.OptionalNamedType('regionalServiceUsed', RegionalServiceUsed().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 54))),
    namedtype.OptionalNamedType('regionDependentChargingOrigin', ChargingOrigin().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 55))),
    namedtype.OptionalNamedType('sSCode', SSCode().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 56))),
    namedtype.OptionalNamedType('channelAllocationPriorityLevel', ChannelAllocationPriorityLevel().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 57))),
    namedtype.OptionalNamedType('radioChannelProperty', RadioChannelProperty().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 58))),
    namedtype.OptionalNamedType('faultCode', FaultCode().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 59))),
    namedtype.OptionalNamedType('intermediateRate', IntermediateRate().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 60))),
    namedtype.OptionalNamedType('firstAssignedSpeechCoderVersion', SpeechCoderVersion().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 61))),
    namedtype.OptionalNamedType('speechCoderPreferenceList', SpeechCoderPreferenceList().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 62))),
    namedtype.OptionalNamedType('subscriptionType', SubscriptionType().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 63))),
    namedtype.OptionalNamedType('incompleteCallDataIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 64))),
    namedtype.OptionalNamedType('incompleteCompositeCDRIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 65))),
    namedtype.OptionalNamedType('switchIdentity', SwitchIdentity().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 67))),
    namedtype.OptionalNamedType('networkCallReference', NetworkCallReference().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 68))),
    namedtype.OptionalNamedType('frequencyBandSupported', FrequencyBandSupported().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 69))),
    namedtype.OptionalNamedType('disconnectionDueToSystemRecovery', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 70))),
    namedtype.OptionalNamedType('forloppDuringOutputIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 71))),
    namedtype.OptionalNamedType('forloppReleaseDuringCall', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 72))),
    namedtype.OptionalNamedType('accountCode', AccountCode().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 73))),
    namedtype.OptionalNamedType('translatedNumber', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 74))),
    namedtype.OptionalNamedType('bCSMTDPData1', CAMELTDPData().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 75))),
    namedtype.OptionalNamedType('bCSMTDPData2', CAMELTDPData().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 76))),
    namedtype.OptionalNamedType('bCSMTDPData3', CAMELTDPData().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 77))),
    namedtype.OptionalNamedType('bCSMTDPData4', CAMELTDPData().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 78))),
    namedtype.OptionalNamedType('bCSMTDPData5', CAMELTDPData().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 79))),
    namedtype.OptionalNamedType('bCSMTDPData6', CAMELTDPData().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 80))),
    namedtype.OptionalNamedType('bCSMTDPData7', CAMELTDPData().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 81))),
    namedtype.OptionalNamedType('bCSMTDPData8', CAMELTDPData().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 82))),
    namedtype.OptionalNamedType('bCSMTDPData9', CAMELTDPData().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 83))),
    namedtype.OptionalNamedType('bCSMTDPData10', CAMELTDPData().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 84))),
    namedtype.OptionalNamedType('gSMCallReferenceNumber', GSMCallReferenceNumber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 85))),
    namedtype.OptionalNamedType('mSCAddress', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 86))),
    namedtype.OptionalNamedType('eMLPPPriorityLevel', EMLPPPriorityLevel().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 87))),
    namedtype.OptionalNamedType('positionAccuracy', PositionAccuracy().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 88))),
    namedtype.OptionalNamedType('userTerminalPosition', UserTerminalPosition().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 89))),
    namedtype.OptionalNamedType('acceptableChannelCodings', ChannelCodings().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 90))),
    namedtype.OptionalNamedType('incomingAssignedRoute', Route().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 91))),
    namedtype.OptionalNamedType('channelCodingUsed', ChannelCodings().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 92))),
    namedtype.OptionalNamedType('rANAPCauseCode', RANAPCauseCode().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 93))),
    namedtype.OptionalNamedType('gsmSCFAddress', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 94))),
    namedtype.OptionalNamedType('fNURRequested', FixedNetworkUserRate().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 95))),
    namedtype.OptionalNamedType('aIURRequested', AirInterfaceUserRate().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 96))),
    namedtype.OptionalNamedType('numberOfChannelsRequested', NumberOfChannels().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 97))),
    namedtype.OptionalNamedType('bSSMAPCauseCode', BSSMAPCauseCode().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 98))),
    namedtype.OptionalNamedType('multimediaCall', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 99))),
    namedtype.OptionalNamedType('guaranteedBitRate', BitRate().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 100))),
    namedtype.OptionalNamedType('trafficClass', TrafficClass().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 101))),
    namedtype.OptionalNamedType('outputType', OutputType().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 102))),
    namedtype.OptionalNamedType('rNCidOfFirstRNC', TargetRNCid().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 103))),
    namedtype.OptionalNamedType('maxBitRateDownlink', BitRate().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 104))),
    namedtype.OptionalNamedType('maxBitRateUplink', BitRate().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 105))),
    namedtype.OptionalNamedType('transferDelay', TransferDelay().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 106))),
    namedtype.OptionalNamedType('deliveryOfErroneousSDU1', DeliveryOfErroneousSDU().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 107))),
    namedtype.OptionalNamedType('deliveryOfErroneousSDU2', DeliveryOfErroneousSDU().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 108))),
    namedtype.OptionalNamedType('deliveryOfErroneousSDU3', DeliveryOfErroneousSDU().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 109))),
    namedtype.OptionalNamedType('residualBitErrorRatio1', ErrorRatio().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 110))),
    namedtype.OptionalNamedType('residualBitErrorRatio2', ErrorRatio().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 111))),
    namedtype.OptionalNamedType('residualBitErrorRatio3', ErrorRatio().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 112))),
    namedtype.OptionalNamedType('sDUErrorRatio1', ErrorRatio().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 113))),
    namedtype.OptionalNamedType('sDUErrorRatio2', ErrorRatio().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 114))),
    namedtype.OptionalNamedType('sDUErrorRatio3', ErrorRatio().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 115))),
    namedtype.OptionalNamedType('aCMChargingIndicator', ChargingIndicator().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 116))),
    namedtype.OptionalNamedType('aNMChargingIndicator', ChargingIndicator().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 117))),
    namedtype.OptionalNamedType('carrierInformationBackward', TransitCarrierInfo().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 118))),
    namedtype.OptionalNamedType('chargeInformation', ChargeInformation().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 119))),
    namedtype.OptionalNamedType('disconnectionDate', Date().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 120))),
    namedtype.OptionalNamedType('disconnectionTime', Time().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 124))),
    namedtype.OptionalNamedType('originatingCarrier', CarrierInfo().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 125))),
    namedtype.OptionalNamedType('originatingChargeArea', ChargeAreaCode().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 126))),
    namedtype.OptionalNamedType('tDSCounter', Counter().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 127))),
    namedtype.OptionalNamedType('terminatingAccessISDN', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 128))),
    namedtype.OptionalNamedType('terminatingCarrier', CarrierInfo().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 129))),
    namedtype.OptionalNamedType('terminatingChargeArea', ChargeAreaCode().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 130))),
    namedtype.OptionalNamedType('terminatingMobileUserClass1', MobileUserClass1().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 131))),
    namedtype.OptionalNamedType('terminatingMobileUserClass2', MobileUserClass2().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 132))),
    namedtype.OptionalNamedType('terminatingUserClass', UserClass().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 133))),
    namedtype.OptionalNamedType('contractorNumber', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 134))),
    namedtype.OptionalNamedType('carrierInformation', CarrierInformation().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 135))),
    namedtype.OptionalNamedType('carrierSelectionSubstitutionInformation', CarrierSelectionSubstitutionInformation().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 136))),
    namedtype.OptionalNamedType('chargeNumber', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 137))),
    namedtype.OptionalNamedType('interExchangeCarrierIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 138))),
    namedtype.OptionalNamedType('originatingLineInformation', OriginatingLineInformation().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 139))),
    namedtype.OptionalNamedType('selectedCodec', SelectedCodec().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 140))),
    namedtype.OptionalNamedType('wPSCallIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 141))),
    namedtype.OptionalNamedType('userToUserInformation', UserToUserInformation().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 142))),
    namedtype.OptionalNamedType('callingSubscriberIMEISV', IMEISV().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 143))),
    namedtype.OptionalNamedType('globalCallReference', GlobalCallReference().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 144))),
    namedtype.OptionalNamedType('roamingPriorityLevel', RoamingPriorityLevel().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 145))),
    namedtype.OptionalNamedType('rTCIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 146))),
    namedtype.OptionalNamedType('rTCSessionID', RTCSessionID().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 147))),
    namedtype.OptionalNamedType('rTCDefaultServiceHandling', RTCDefaultServiceHandling().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 148))),
    namedtype.OptionalNamedType('rTCFailureIndicator', RTCFailureIndicator().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 149))),
    namedtype.OptionalNamedType('rTCNotInvokedReason', RTCNotInvokedReason().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 150))),
    namedtype.OptionalNamedType('originatedCode', OriginatedCode().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 66))),
    namedtype.OptionalNamedType('reroutingIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 121))),
    namedtype.OptionalNamedType('invocationOfCallHold', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 122))),
    namedtype.OptionalNamedType('retrievalOfHeldCall', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 123))),

    namedtype.OptionalNamedType('privateType195', univ.OctetString().subtype(implicitTag=tag.Tag(tag.tagClassPrivate, tag.tagFormatConstructed, 195))),
  )


class SSIEventModule(univ.Set):
  componentType = namedtype.NamedTypes(
    namedtype.OptionalNamedType('tAC', TAC().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0))),
    namedtype.OptionalNamedType('sSCode', SSCode().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1))),
    namedtype.OptionalNamedType('sSRequest', SSRequest().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2))),
    namedtype.OptionalNamedType('timeForEvent', Time().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3))),
    namedtype.OptionalNamedType('firstCallingLocationInformation', LocationInformation().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4))),
    namedtype.OptionalNamedType('cRIIndicator', CRIIndicator().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 5))),
    namedtype.OptionalNamedType('eventCRIToMS', EventCRIToMS().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 6))),
    namedtype.OptionalNamedType('incompleteCallDataIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 7))),
    namedtype.OptionalNamedType('networkCallReference', NetworkCallReference().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 9))),
    namedtype.OptionalNamedType('sSInvocationNotification', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 10))),
    namedtype.OptionalNamedType('globalCallReference', GlobalCallReference().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 11))),

    namedtype.OptionalNamedType('privateType195', univ.OctetString().subtype(implicitTag=tag.Tag(tag.tagClassPrivate, tag.tagFormatConstructed, 195))),
  )


class MSTerminatingSMSinSMS_GMSC(univ.Set):
  componentType = namedtype.NamedTypes(
    namedtype.OptionalNamedType('tAC', TAC().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0))),
    namedtype.OptionalNamedType('callIdentificationNumber', CallIDNumber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1))),
    namedtype.OptionalNamedType('recordSequenceNumber', RecordSequenceNumber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2))),
    namedtype.OptionalNamedType('calledPartyNumber', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3))),
    namedtype.OptionalNamedType('calledSubscriberIMSI', IMSI().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4))),
    namedtype.OptionalNamedType('mobileStationRoamingNumber', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 5))),
    namedtype.OptionalNamedType('dateForStartOfCharge', Date().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 6))),
    namedtype.OptionalNamedType('timeForStartOfCharge', Time().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 7))),
    namedtype.OptionalNamedType('chargedParty', ChargedParty().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 8))),
    namedtype.OptionalNamedType('exchangeIdentity', ExchangeIdentity().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 9))),
    namedtype.OptionalNamedType('mSCIdentification', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 10))),
    namedtype.OptionalNamedType('teleServiceCode', TeleServiceCode().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 11))),
    namedtype.OptionalNamedType('serviceCentreAddress', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 12))),
    namedtype.OptionalNamedType('mSCNumber', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 13))),
    namedtype.OptionalNamedType('miscellaneousInformation', MiscellaneousInformation().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 14))),
    namedtype.OptionalNamedType('incompleteCallDataIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 15))),
    namedtype.OptionalNamedType('restartDuringOutputIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 16))),
    namedtype.OptionalNamedType('forloppDuringOutputIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 17))),
    namedtype.OptionalNamedType('numberOfShortMessages', NumberOfShortMessage().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 18))),
    namedtype.OptionalNamedType('switchIdentity', SwitchIdentity().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 19))),
    namedtype.OptionalNamedType('outputType', OutputType().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 102))),

    namedtype.OptionalNamedType('privateType195', univ.OctetString().subtype(implicitTag=tag.Tag(tag.tagClassPrivate, tag.tagFormatConstructed, 195))),
  )


class LocationServices(univ.Set):
  componentType = namedtype.NamedTypes(
    namedtype.OptionalNamedType('tAC', TAC().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0))),
    namedtype.OptionalNamedType('callIdentificationNumber', CallIDNumber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1))),
    namedtype.OptionalNamedType('recordSequenceNumber', RecordSequenceNumber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2))),
    namedtype.OptionalNamedType('typeOfCallingSubscriber', TypeOfCallingSubscriber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3))),
    namedtype.OptionalNamedType('targetMSISDN', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4))),
    namedtype.OptionalNamedType('targetIMSI', IMSI().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 5))),
    namedtype.OptionalNamedType('targetIMEI', IMEI().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 6))),
    namedtype.OptionalNamedType('dateForStartOfCharge', Date().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 7))),
    namedtype.OptionalNamedType('timeForStartOfCharge', Time().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 8))),
    namedtype.OptionalNamedType('exchangeIdentity', ExchangeIdentity().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 9))),
    namedtype.OptionalNamedType('mSCIdentification', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 10))),
    namedtype.OptionalNamedType('miscellaneousInformation', MiscellaneousInformation().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 11))),
    namedtype.OptionalNamedType('restartDuringOutputIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 12))),
    namedtype.OptionalNamedType('iCIOrdered', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 13))),
    namedtype.OptionalNamedType('outputForSubscriber', OutputForSubscriber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 14))),
    namedtype.OptionalNamedType('incompleteCallDataIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 15))),
    namedtype.OptionalNamedType('switchIdentity', SwitchIdentity().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 16))),
    namedtype.OptionalNamedType('networkCallReference', NetworkCallReference().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 17))),
    namedtype.OptionalNamedType('forloppDuringOutputIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 18))),
    namedtype.OptionalNamedType('positioningDelivery', PositioningDelivery().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 19))),
    namedtype.OptionalNamedType('lCSClientIdentity', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 20))),
    namedtype.OptionalNamedType('lCSClientType', LCSClientType().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 21))),
    namedtype.OptionalNamedType('locationEstimate', LocationEstimate().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 22))),
    namedtype.OptionalNamedType('ageOfLocationEstimate', AgeOfLocationEstimate().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 23))),
    namedtype.OptionalNamedType('subscriberState', SubscriberState().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 24))),
    namedtype.OptionalNamedType('mLCAddress', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 25))),
    namedtype.OptionalNamedType('decipheringKeys', DecipheringKeys().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 26))),
    namedtype.OptionalNamedType('typeOfLocationRequest', TypeOfLocationRequest().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 27))),
    namedtype.OptionalNamedType('firstTargetLocationInformation', LocationInformation().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 28))),
    namedtype.OptionalNamedType('horizontalAccuracy', LCSAccuracy().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 29))),
    namedtype.OptionalNamedType('responseTimeCategory', ResponseTimeCategory().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 30))),
    namedtype.OptionalNamedType('verticalAccuracy', LCSAccuracy().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 31))),
    namedtype.OptionalNamedType('verticalCoordinateRequest', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 32))),
    namedtype.OptionalNamedType('unsuccessfulPositioningDataReason', UnsuccessfulPositioningDataReason().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 33))),
    namedtype.OptionalNamedType('lCSDeferredEventType', LCSDeferredEventType().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 34))),
    namedtype.OptionalNamedType('targetIMEISV', IMEISV().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 35))),
    namedtype.OptionalNamedType('globalCallReference', GlobalCallReference().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 36))),
    namedtype.OptionalNamedType('outputType', OutputType().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 102))),

    namedtype.OptionalNamedType('privateType195', univ.OctetString().subtype(implicitTag=tag.Tag(tag.tagClassPrivate, tag.tagFormatConstructed, 195))),
  )


class MSTerminatingSMSinMSC(univ.Set):
  componentType = namedtype.NamedTypes(
    namedtype.OptionalNamedType('tAC', TAC().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0))),
    namedtype.OptionalNamedType('callIdentificationNumber', CallIDNumber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1))),
    namedtype.OptionalNamedType('recordSequenceNumber', RecordSequenceNumber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2))),
    namedtype.OptionalNamedType('calledPartyNumber', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3))),
    namedtype.OptionalNamedType('calledSubscriberIMSI', IMSI().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4))),
    namedtype.OptionalNamedType('calledSubscriberIMEI', IMEI().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 5))),
    namedtype.OptionalNamedType('dateForStartOfCharge', Date().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 6))),
    namedtype.OptionalNamedType('timeForStartOfCharge', Time().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 7))),
    namedtype.OptionalNamedType('originForCharging', ChargingOrigin().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 8))),
    namedtype.OptionalNamedType('chargedParty', ChargedParty().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 9))),
    namedtype.OptionalNamedType('exchangeIdentity', ExchangeIdentity().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 10))),
    namedtype.OptionalNamedType('mSCIdentification', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 11))),
    namedtype.OptionalNamedType('outgoingRoute', Route().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 12))),
    namedtype.OptionalNamedType('firstCalledLocationInformation', LocationInformation().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 13))),
    namedtype.OptionalNamedType('teleServiceCode', TeleServiceCode().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 14))),
    namedtype.OptionalNamedType('serviceCentreAddress', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 15))),
    namedtype.OptionalNamedType('iCIOrdered', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 18))),
    namedtype.OptionalNamedType('outputForSubscriber', OutputForSubscriber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 19))),
    namedtype.OptionalNamedType('miscellaneousInformation', MiscellaneousInformation().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 20))),
    namedtype.OptionalNamedType('regionalServiceUsed', RegionalServiceUsed().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 21))),
    namedtype.OptionalNamedType('regionDependentChargingOrigin', ChargingOrigin().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 22))),
    namedtype.OptionalNamedType('channelAllocationPriorityLevel', ChannelAllocationPriorityLevel().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 23))),
    namedtype.OptionalNamedType('incompleteCallDataIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 24))),
    namedtype.OptionalNamedType('restartDuringOutputIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 25))),
    namedtype.OptionalNamedType('frequencyBandSupported', FrequencyBandSupported().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 26))),
    namedtype.OptionalNamedType('forloppDuringOutputIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 27))),
    namedtype.OptionalNamedType('numberOfShortMessages', NumberOfShortMessage().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 28))),
    namedtype.OptionalNamedType('lastCalledLocationInformation', LocationInformation().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 29))),
    namedtype.OptionalNamedType('positionAccuracy', PositionAccuracy().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 30))),
    namedtype.OptionalNamedType('userTerminalPosition', UserTerminalPosition().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 31))),
    namedtype.OptionalNamedType('switchIdentity', SwitchIdentity().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 32))),
    namedtype.OptionalNamedType('originatingAddress', AddressStringExtended().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 33))),
    namedtype.OptionalNamedType('messageTypeIndicator', MessageTypeIndicator().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 34))),
    namedtype.OptionalNamedType('rNCidOfFirstRNC', TargetRNCid().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 35))),
    namedtype.OptionalNamedType('bCSMTDPData1', CAMELTDPData().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 36))),
    namedtype.OptionalNamedType('defaultSMSHandling', DefaultSMS_Handling().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 37))),
    namedtype.OptionalNamedType('freeFormatData', FreeFormatData().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 38))),
    namedtype.OptionalNamedType('sMSResult', SMSResult().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 39))),
    namedtype.OptionalNamedType('sMSReferenceNumber', GSMCallReferenceNumber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 40))),
    namedtype.OptionalNamedType('mSCAddress', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 41))),
    namedtype.OptionalNamedType('cAMELOriginatingAddress', AddressStringExtended().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 42))),
    namedtype.OptionalNamedType('calledSubscriberIMEISV', IMEISV().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 43))),
    namedtype.OptionalNamedType('rTCIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 44))),
    namedtype.OptionalNamedType('rTCSessionID', RTCSessionID().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 45))),
    namedtype.OptionalNamedType('rTCDefaultServiceHandling', RTCDefaultServiceHandling().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 46))),
    namedtype.OptionalNamedType('rTCFailureIndicator', RTCFailureIndicator().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 47))),
    namedtype.OptionalNamedType('rTCNotInvokedReason', RTCNotInvokedReason().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 48))),
    namedtype.OptionalNamedType('outputType', OutputType().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 102))),

    namedtype.OptionalNamedType('privateType195', univ.OctetString().subtype(implicitTag=tag.Tag(tag.tagClassPrivate, tag.tagFormatConstructed, 195))),
  )


class INOutgoingCall(univ.Set):
  componentType = namedtype.NamedTypes(
    namedtype.OptionalNamedType('callIdentificationNumber', CallIDNumber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0))),
    namedtype.OptionalNamedType('switchIdentity', SwitchIdentity().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1))),
    namedtype.OptionalNamedType('networkCallReference', NetworkCallReference().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2))),
    namedtype.OptionalNamedType('iNServiceTrigger', INServiceTrigger().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3))),
    namedtype.OptionalNamedType('sSFChargingCase', SSFChargingCase().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4))),
    namedtype.OptionalNamedType('triggerData0', TriggerData().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 5))),
    namedtype.OptionalNamedType('triggerData1', TriggerData().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 6))),
    namedtype.OptionalNamedType('triggerData2', TriggerData().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 7))),
    namedtype.OptionalNamedType('triggerData3', TriggerData().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 8))),
    namedtype.OptionalNamedType('triggerData4', TriggerData().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 9))),
    namedtype.OptionalNamedType('triggerData5', TriggerData().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 10))),
    namedtype.OptionalNamedType('triggerData6', TriggerData().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 11))),
    namedtype.OptionalNamedType('triggerData7', TriggerData().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 12))),
    namedtype.OptionalNamedType('recordSequenceNumber', RecordSequenceNumber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 13))),
    namedtype.OptionalNamedType('disconnectionDueToSystemRecovery', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 14))),
    namedtype.OptionalNamedType('incompleteCallDataIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 15))),
    namedtype.OptionalNamedType('incompleteCompositeCDRIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 16))),
    namedtype.OptionalNamedType('lastPartialOutput', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 17))),
    namedtype.OptionalNamedType('partialOutputRecNum', PartialOutputRecNum().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 18))),
    namedtype.OptionalNamedType('restartDuringOutputIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 19))),
    namedtype.OptionalNamedType('restartDuringCall', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 20))),
    namedtype.OptionalNamedType('exchangeIdentity', ExchangeIdentity().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 21))),
    namedtype.OptionalNamedType('forloppDuringOutputIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 22))),
    namedtype.OptionalNamedType('forloppReleaseDuringCall', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 23))),
    namedtype.OptionalNamedType('gSMCallReferenceNumber', GSMCallReferenceNumber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 24))),
    namedtype.OptionalNamedType('mSCAddress', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 25))),
    namedtype.OptionalNamedType('defaultCallHandling', DefaultCallHandling().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 26))),
    namedtype.OptionalNamedType('defaultCallHandling2', DefaultCallHandling().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 27))),
    namedtype.OptionalNamedType('levelOfCAMELService', LevelOfCAMELService().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 28))),
    namedtype.OptionalNamedType('gsmSCFInitiatedCallIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 29))),
    namedtype.OptionalNamedType('globalCallReference', GlobalCallReference().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 30))),
    namedtype.OptionalNamedType('outputType', OutputType().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 102))),
  )


class INIncomingCall(univ.Set):
  componentType = namedtype.NamedTypes(
    namedtype.OptionalNamedType('callIdentificationNumber', CallIDNumber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0))),
    namedtype.OptionalNamedType('switchIdentity', SwitchIdentity().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1))),
    namedtype.OptionalNamedType('networkCallReference', NetworkCallReference().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2))),
    namedtype.OptionalNamedType('iNServiceTrigger', INServiceTrigger().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3))),
    namedtype.OptionalNamedType('sSFChargingCase', SSFChargingCase().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4))),
    namedtype.OptionalNamedType('triggerData0', TriggerData().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 5))),
    namedtype.OptionalNamedType('triggerData1', TriggerData().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 6))),
    namedtype.OptionalNamedType('triggerData2', TriggerData().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 7))),
    namedtype.OptionalNamedType('triggerData3', TriggerData().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 8))),
    namedtype.OptionalNamedType('triggerData4', TriggerData().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 9))),
    namedtype.OptionalNamedType('triggerData5', TriggerData().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 10))),
    namedtype.OptionalNamedType('triggerData6', TriggerData().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 11))),
    namedtype.OptionalNamedType('triggerData7', TriggerData().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 12))),
    namedtype.OptionalNamedType('recordSequenceNumber', RecordSequenceNumber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 13))),
    namedtype.OptionalNamedType('disconnectionDueToSystemRecovery', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 14))),
    namedtype.OptionalNamedType('incompleteCallDataIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 15))),
    namedtype.OptionalNamedType('incompleteCompositeCDRIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 16))),
    namedtype.OptionalNamedType('lastPartialOutput', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 17))),
    namedtype.OptionalNamedType('partialOutputRecNum', PartialOutputRecNum().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 18))),
    namedtype.OptionalNamedType('restartDuringOutputIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 19))),
    namedtype.OptionalNamedType('restartDuringCall', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 20))),
    namedtype.OptionalNamedType('exchangeIdentity', ExchangeIdentity().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 21))),
    namedtype.OptionalNamedType('forloppDuringOutputIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 22))),
    namedtype.OptionalNamedType('forloppReleaseDuringCall', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 23))),
    namedtype.OptionalNamedType('gSMCallReferenceNumber', GSMCallReferenceNumber().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 24))),
    namedtype.OptionalNamedType('mSCAddress', AddressString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 25))),
    namedtype.OptionalNamedType('defaultCallHandling', DefaultCallHandling().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 26))),
    namedtype.OptionalNamedType('defaultCallHandling2', DefaultCallHandling().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 27))),
    namedtype.OptionalNamedType('levelOfCAMELService', LevelOfCAMELService().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 28))),
    namedtype.OptionalNamedType('globalCallReference', GlobalCallReference().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 29))),
    namedtype.OptionalNamedType('outputType', OutputType().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 102))),
  )


class AoCEventModule(univ.Set):
  componentType = namedtype.NamedTypes(
    namedtype.OptionalNamedType('tAC', TAC().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0))),
    namedtype.OptionalNamedType('cRIToMS', CRIToMS().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1))),
    namedtype.OptionalNamedType('cRIIndicator', CRIIndicator().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2))),
    namedtype.OptionalNamedType('sSCode', SSCode().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3))),
    namedtype.OptionalNamedType('timeForEvent', Time().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4))),
    namedtype.OptionalNamedType('incompleteCallDataIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 5))),
    namedtype.OptionalNamedType('gsmSCFControlOfAoC', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 6))),
  )


class INServiceDataEventModule(univ.Set):
  componentType = namedtype.NamedTypes(
    namedtype.OptionalNamedType('chargePartyDistributed', Distributed().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0))),
    namedtype.OptionalNamedType('chargePartySingle', Single().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1))),
    namedtype.OptionalNamedType('chargingUnitsAddition', ChargingUnitsAddition().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2))),
    namedtype.OptionalNamedType('genericChargingDigits', GenericDigitsSet().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3))),
    namedtype.OptionalNamedType('genericChargingNumbers', GenericNumbersSet().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4))),
    namedtype.OptionalNamedType('serviceFeatureCode', ServiceFeatureCode().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 5))),
    namedtype.OptionalNamedType('timeForEvent', Time().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 6))),
    namedtype.OptionalNamedType('incompleteCallDataIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 7))),
    namedtype.OptionalNamedType('freeFormatData', FreeFormatData().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 8))),
    namedtype.OptionalNamedType('sSFLegID', LegID().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 9))),
    namedtype.OptionalNamedType('freeFormatData2', FreeFormatData().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 10))),
    namedtype.OptionalNamedType('freeFormatDataAppendIndicator', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 11))),
    namedtype.OptionalNamedType('freeFormatDataAppendIndicator2', univ.Null().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 12))),
  )

class EventModule(univ.Choice):
  componentType = namedtype.NamedTypes(
    namedtype.NamedType('aoCEventModule', AoCEventModule().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 10))),
    namedtype.NamedType('sSInvocationEventModule', SSIEventModule().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 11))),
    namedtype.NamedType('serviceSwitchEventModule', ServiceSwitchEventModule().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 12))),
    namedtype.NamedType('iNServiceDataEventModule', INServiceDataEventModule().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 16))),
    namedtype.NamedType('chargeRateChangeEventModule', ChargeRateChangeEventModule().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 20))),
    namedtype.NamedType('iSDNSSInvocationEventModule', ISDNSSInvocationEventModule().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 23))),
    namedtype.NamedType('handOverEventModule', HandOverEventModule().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 25))),
  )

class UMTSGSMPLMNCallDataRecord(univ.Sequence):
  tagSet = univ.Sequence.tagSet.tagImplicitly(
    tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))

  componentType = namedtype.NamedTypes(
    namedtype.NamedType('u', univ.Choice(
      componentType = namedtype.NamedTypes(
        namedtype.NamedType('transit', Transit().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0))),
        namedtype.NamedType('mSOriginating', MSOriginating().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1))),
        namedtype.NamedType('roamingCallForwarding', RoamingCallForwarding().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2))),
        namedtype.NamedType('callForwarding', CallForwarding().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3))),
        namedtype.NamedType('mSTerminating', MSTerminating().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4))),
        namedtype.NamedType('mSOriginatingSMSinMSC', MSOriginatingSMSinMSC().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 5))),
        namedtype.NamedType('mSOriginatingSMSinSMS_IWMSC', MSOriginatingSMSinSMS_IWMSC().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 6))),
        namedtype.NamedType('mSTerminatingSMSinMSC', MSTerminatingSMSinMSC().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 7))),
        namedtype.NamedType('mSTerminatingSMSinSMS_GMSC', MSTerminatingSMSinSMS_GMSC().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 8))),
        namedtype.NamedType('sSProcedure', SSProcedure().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 9))),
        namedtype.NamedType('transitINOutgoingCall', TransitINOutgoingCall().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 13))),
        namedtype.NamedType('iNIncomingCall', INIncomingCall().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 14))),
        namedtype.NamedType('iNOutgoingCall', INOutgoingCall().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 15))),
        namedtype.NamedType('iSDNOriginating', ISDNOriginating().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 17))),
        namedtype.NamedType('iSDNCallForwarding', ISDNCallForwarding().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 18))),
        namedtype.NamedType('iSDNSSProcedure', ISDNSSProcedure().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 19))),
        namedtype.NamedType('sCFChargingOutput', SCFChargingOutput().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 21))),
        namedtype.NamedType('locationServices', LocationServices().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 24))),
      ))),
    namedtype.OptionalNamedType('eventModule', univ.SequenceOf(componentType=EventModule())),
  )


class CompositeCallDataRecord(univ.SequenceOf):
  componentType = UMTSGSMPLMNCallDataRecord()

class CallDataRecord(univ.Choice):
  componentType = namedtype.NamedTypes(
    namedtype.NamedType('uMTSGSMPLMNCallDataRecord', UMTSGSMPLMNCallDataRecord()),
    namedtype.NamedType('compositeCallDataRecord', CompositeCallDataRecord().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
  )

